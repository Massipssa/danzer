from marshmallow import Schema, fields, ValidationError


class OperationSchema(Schema):
    name = fields.Str(required=True)
    algorithm_name = fields.Str(required=True)
    columns = fields.List(fields.Str(), required=True)


class DataSourceSchema(Schema):
    name = fields.Str(required=True)
    bucket = fields.Str()
    path = fields.Str()


class ExecutionEngineSchema(Schema):
    name = fields.Str(required=True)


class ConfigSchema(Schema):
    name = fields.Str(required=True)
    operation = fields.Nested(OperationSchema, required=True)
    data_source = fields.Nested(DataSourceSchema, required=True)
    execution_engine = fields.Nested(ExecutionEngineSchema, required=True)


## TODO: rename
def load_config(config_data):
    try:
        schema = ConfigSchema()
        config = schema.load(config_data)
        return config
    except ValidationError as e:
        raise ValueError(f"Invalid configuration: {e.messages}")
