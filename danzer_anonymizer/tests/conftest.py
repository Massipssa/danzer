import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="module")
def spark_session():
    spark = SparkSession.builder \
        .appName("pytest_spark_session") \
        .config("spark.master", "local[2]") \
        .getOrCreate()
    yield spark
    spark.stop()
