import pytest
from pyspark.sql import SparkSession

from danzer.anonymizer.core.anonymization.column_suppression import ColumnSuppression
from danzer.anonymizer.core.engine.execution_engine import EngineType


@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local[1]").appName("ColumnSuppressionTest").getOrCreate()


def test_suppress_columns_spark(spark):
    # Sample Spark DataFrame
    data = [("Alice", 30, "HR"), ("Bob", 35, "IT")]
    columns = ["name", "age", "department"]
    df = spark.createDataFrame(data, schema=columns)

    params = {
        "operation": {
            "columns_to_delete": ["age"]
        }
    }

    suppressor = ColumnSuppression(
        df=df,
        params=params,
        inplace=False,
        engine_type=EngineType.SPARK
    )

    suppressor.validate(params)  # normally called by operate()
    result_df = suppressor._suppress_columns_spark()

    # Collect and test schema
    result_columns = result_df.columns
    assert "age" not in result_columns
    assert "name" in result_columns
    assert "department" in result_columns
    assert len(result_columns) == 2

    # Optional: verify row content
    rows = result_df.collect()
    assert rows[0]["name"] == "Alice"
    assert rows[1]["department"] == "IT"
