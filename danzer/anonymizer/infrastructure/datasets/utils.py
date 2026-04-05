import logging
from typing import Dict, Optional

from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)


def get_or_create_spark_session(spark_config: Optional[Dict[str, str]] = None) -> SparkSession | None:
    """Create a Spark session if needed and return it."""
    try:
        builder = SparkSession.builder
        for key, value in (spark_config or {}).items():
            builder = builder.config(key, value)
        return builder.getOrCreate()
    except Exception:
        logger.exception("Unable to create Spark session")
        return None
