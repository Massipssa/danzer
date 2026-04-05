import pytest
import pandas as pd

from pyspark.sql import SparkSession

from danzer.anonymizer.core.anonymization.column_suppression import ColumnSuppression
from danzer.anonymizer.core.engine.execution_engine import EngineType


@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local[1]").appName("ColumnSuppressionTest").getOrCreate()

