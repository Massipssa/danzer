from flask import Flask

from danzer_anonymizer.danzer_anonymizer.models.expectation import db

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


@app.route("/expectations")
def get_expectations():
    return []


@app.route('/expectations', methods=['POST'])
def add_expectation():
    return []


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
