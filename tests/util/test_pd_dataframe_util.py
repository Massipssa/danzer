import pandas as pd

import pytest

from data_anonymizer.exceptions.exceptions import DataAnonymizerExpectationsError
from data_anonymizer.util.pd_dataframe_util import all_columns_name_are_valid


@pytest.fixture
def test_pandas_dataframe():
    data = {'col_a': [1, 2, 3], 'col_b': [4, 5, 6], 'col_c': [7, 8, 9]}
    return pd.DataFrame(data)


def test_all_columns_name_are_valid(test_pandas_dataframe):
    valid_columns = ['col_a', 'col_b', 'col_c']
    columns_are_valid = all_columns_name_are_valid(test_pandas_dataframe, valid_columns)
    assert columns_are_valid


def test_raises_exception_when_invalid_columns(test_pandas_dataframe):
    invalid_columns = ['fake_col1', 'fake_col2']
    with pytest.raises(DataAnonymizerExpectationsError) as e:
        all_columns_name_are_valid(test_pandas_dataframe, invalid_columns)
    #invalid_columns = list(invalid_columns)
    assert len(str(e.value)) > 0 # == f"Columns {list(invalid_columns)} are not present in the DataFrame."
