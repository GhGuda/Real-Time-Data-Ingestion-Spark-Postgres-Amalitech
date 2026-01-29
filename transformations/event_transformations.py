from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType


def transform_events(df):
    """
    Apply transformations to raw event data.
    """
    return (
        df
        .withColumn("price", col("price").cast(DoubleType()))
        .select(
            "event",
            "user_name",
            "product",
            "price",
            "event_time"
        )
    )
