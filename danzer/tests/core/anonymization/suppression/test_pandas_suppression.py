import pandas as pd

from danzer.anonymizer.core.anonymization.suppression.pandas_suppression import PandasSuppressRule


def test_suppress_columns_pandas_inplace_true():
    df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [30, 35],
        "city": ["Paris", "London"]
    })

    params = {
        "operation": {
            "columns_to_delete": ["age"]
        }
    }

    pandas_suppress_rule = PandasSuppressRule(
        columns=["age"],
        params=params,
        inplace=True
    )

    result = pandas_suppress_rule.apply(df)

    assert result is None
    assert "age" not in df.columns
    assert "name" in df.columns
    assert "city" in df.columns


def test_suppress_columns_pandas_inplace_false():
    df = pd.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [30, 35],
        "city": ["Paris", "London"]
    })

    params = {
        "operation": {
            "columns_to_delete": ["city"]
        }
    }

    pandas_suppress_rule = PandasSuppressRule(
        columns=[],
        params=params,
        inplace=False
    )
    result = pandas_suppress_rule.apply(df)

    assert "city" not in result.columns
    assert "city" in df.columns
    assert "name" in result.columns
    assert "age" in result.columns


def test_suppress_columns_pandas_invalid_column(caplog):
    df = pd.DataFrame({
        "name": ["Alice"],
        "email": ["alice@example.com"]
    })

    params = {
        "operation": {
            "columns_to_delete": ["nonexistent"]
        }
    }

    pandas_suppress_rule = PandasSuppressRule(
        columns=[],
        params=params,
        inplace=True
    )

    result = pandas_suppress_rule.apply(df)

    assert result.equals(df)
