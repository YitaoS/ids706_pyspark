"""
Main cli or app entry point
"""

from mylib.lib import (
    extract,
    load_data,
    describe,
    query,
    example_transform,
    start_spark,
    end_spark,
)


def main():
    # extract data
    extract()
    # start spark session
    spark = start_spark("DailyShowGuests")
    # load data into dataframe
    df = load_data(spark)
    # example metrics
    describe(df)
    # query
    query(
        spark,
        df,
        """
        SELECT city, ROUND((jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec) / 12, 2) AS yearly_avg 
        FROM city_temperatures
        ORDER BY yearly_avg DESC
        """,
        "city_temperatures"
    )
    # example transform
    example_transform(df)
    # end spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
