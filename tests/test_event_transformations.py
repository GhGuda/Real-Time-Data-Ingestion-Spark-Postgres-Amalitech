from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType
from transformations.event_transformations import transform_events


def test_event_transformation_logic():
    spark = (
        SparkSession.builder
        .master("local[1]")
        .appName("event-transformation-test")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("ERROR")

    # -----------------------------
    # Input schema (raw CSV-like)
    # -----------------------------
    schema = StructType([
        StructField("event", StringType(), True),
        StructField("user_name", StringType(), True),
        StructField("product", StringType(), True),
        StructField("price", StringType(), True),
        StructField("event_time", StringType(), True),
    ])

    data = [
        ("purchase", "Ama", "Laptop", "2500.50", "2026-01-28 20:00:00")
    ]

    df = spark.createDataFrame(data, schema=schema)

    # -----------------------------
    # Apply transformation
    # -----------------------------
    result_df = transform_events(df)

    result = result_df.collect()[0]

    # -----------------------------
    # Assertions
    # -----------------------------
    assert result["price"] == 2500.50
    assert isinstance(result["price"], float)

    expected_columns = [
        "event",
        "user_name",
        "product",
        "price",
        "event_time",
    ]
    assert result_df.columns == expected_columns

    spark.stop()
