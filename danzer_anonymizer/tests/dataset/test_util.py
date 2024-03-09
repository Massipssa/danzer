import pytest
from pyspark.sql import SparkSession

from danzer_anonymizer.anonymizer.dataset.util import get_or_create_spark_session


@pytest.mark.skip
def test_get_or_create_spark_session(spark_session):
    test_spark_session = get_or_create_spark_session(None)
    assert test_spark_session is not None
    assert isinstance(test_spark_session, SparkSession)
    assert test_spark_session.version.startswith("3.")
