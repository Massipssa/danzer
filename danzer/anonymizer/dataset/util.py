import logging
from typing import Dict, Optional

from pyspark.sql import SparkSession

logger = logging.getLogger(__name__)


def get_or_create_spark_session(spark_config: Optional[Dict[str, str]] = None) -> SparkSession | None:
    """
    Create spark session if it doesn't exist or get the existing one
    """
    spark_session: Optional[SparkSession]
    try:
        builder = SparkSession.builder
        for k, v in spark_config:
            builder.config(k, v)
        spark_session = builder.getOrCreate()
    except ArithmeticError:
        logger.error("")
        spark_session = None
    return spark_session
