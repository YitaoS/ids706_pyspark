"""
Test suite for PySpark application
"""
import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)

@pytest.fixture(scope="module")
def spark():
    spark = start_spark("TestApp")
    yield spark
    end_spark(spark)

def test_extract():
    file_path = extract(
        url="https://path_to_your_new_data.csv",  # Update to actual URL
        file_path="data/new_data.csv"
    )
    assert os.path.exists(file_path) is True

def test_load_data(spark):
    df = load_data(spark, data="data/new_data.csv")
    assert df is not None
    assert "rank" in df.columns
    assert "city" in df.columns

def test_describe(spark):
    df = load_data(spark, data="data/new_data.csv")
    result = describe(df)
    assert result is None  # describe() has no return

def test_query(spark):
    df = load_data(spark, data="data/new_data.csv")
    # Example query adjusted to new data format
    result = query(
        spark, df, "SELECT city, avg FROM city_temperatures WHERE avg > 200", "city_temperatures"
    )
    assert result is None  # query() has no return

def test_example_transform(spark):
    df = load_data(spark, data="data/new_data.csv")
    result = example_transform(df)
    assert result is None  # example_transform() has no return

if __name__ == "__main__":
    test_extract()
    test_load_data(spark())
    test_describe(spark())
    test_query(spark())
    test_example_transform(spark())
