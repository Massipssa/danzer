import logging.config

from api.product import db, Product
from flask import Flask, jsonify, request
from sqlalchemy import exc

# Configure the logging package from the logging ini file
# logging.config.fileConfig("logging.ini", disable_existing_loggers=False)

# Get a logger for our module
log = logging.getLogger(__name__)

app = Flask(__name__)

DB_USER = 'testuser'
DB_PASSWORD = 'testpwd'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'db'
DB_URL = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/products')
def get_products():
    log.debug('GET /products')
    try:
        products = [product.json for product in Product.find_all()]
        return jsonify(products)
    except exc.SQLAlchemyError:
        log.exception('An exception occurred while retrieving all products')
        return 'An exception occurred while retrieving all products', 500


@app.route('/product/<int:id>')
def get_product(id: int):
    log.debug(f'GET /product/{id}')

    try:
        product = Product.find_by_id(id)
        if product:
            return jsonify(product.json)
        log.warning(f'GET /product/{id}: Product not found')
        return f'Product with id {id} not found', 404
    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while retrieving product {id}')
        return f'An exception occurred while retrieving product {id}', 500


@app.route('/product', methods=['POST'])
def post_product():
    # Retrieve the product from the request body
    request_product = request.json
    log.debug(f'POST /products with product: {request_product}')

    # Create a new Product
    product = Product(None, request_product['name'])

    try:
        # Save the Product to the database
        product.save_to_db()

        # Return the jsonified Product
        return jsonify(product.json), 201
    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while creating product with name: {product.name}')
        return f'An exception occurred while creating product with name: {product.name}', 500


# curl --header "Content-Type: application/json" --request PUT --data '{"name": "Updated Product 2"}' -v
@app.route('/product/<int:id>', methods=['PUT'])
def put_product(id: int):
    log.debug(f'PUT /product/{id}')
    try:
        existing_product = Product.find_by_id(id)

        if existing_product:
            # Get the request payload
            updated_product = request.json

            existing_product.name = updated_product['name']
            existing_product.save_to_db()

            return jsonify(existing_product.json), 200

        log.warning(f'PUT /product/{id}: Existing product not found')
        return f'Product with id {id} not found', 404

    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while updating product with name: {updated_product.name}')
        return f'An exception occurred while updating product with name: {updated_product.name}', 500


@app.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id: int):
    log.debug(f'DELETE /product/{id}')
    try:
        existing_product = Product.find_by_id(id)
        if existing_product:
            existing_product.delete_from_db()
            return jsonify({
                'message': f'Deleted product with id {id}'
            }), 200

        log.warning(f'DELETE /product/{id}: Existing product not found')
        return f'Product with id {id} not found', 404

    except exc.SQLAlchemyError:
        log.exception(f'An exception occurred while deleting the product with id: {id}')
        return f'An exception occurred while deleting the product with id: {id}', 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
