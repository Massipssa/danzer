import sys

import pytest
import pyspark


@pytest.mark.skipif(
    sys.version_info >= (3, 11) and tuple(int(part) for part in pyspark.__version__.split(".")[:2]) < (3, 4),
    reason="PySpark < 3.4 is not reliable on Python 3.11 in this environment."
)
def test_suppress_columns_spark(spark):
    from danzer.anonymizer.core.anonymization.column_suppression import ColumnSuppression
    from danzer.anonymizer.core.engine.execution_engine import EngineType

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

    suppressor.validate(params)
    result_df = suppressor._suppress_columns_spark()

    result_columns = result_df.columns
    assert "age" not in result_columns
    assert "name" in result_columns
    assert "department" in result_columns
    assert len(result_columns) == 2

    rows = result_df.collect()
    assert rows[0]["name"] == "Alice"
    assert rows[1]["department"] == "IT"
