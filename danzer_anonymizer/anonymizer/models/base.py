from typing import Any

from sqlalchemy import MetaData

from sqlalchemy.orm import registry

schema = "test"


def _get_schema():
    if not schema or schema.isspace():
        return None
    else:
        return schema


metadata = MetaData(schema=_get_schema())
mapper_registry = registry(metadata)

Base: Any = mapper_registry.generate_base(metadata=metadata)
