
from pyspark.sql.types import (
    StringType,
    DoubleType,
    TimestampType,
)


def get_postgres_events_schema():
    """
    Expected PostgreSQL schema for the events table.
    (id is excluded because it is BIGSERIAL in Postgres)
    """
    return {
        "event": StringType(),
        "user_name": StringType(),
        "product": StringType(),
        "price": DoubleType(),
        "event_time": TimestampType(),
        "source_file": StringType(),
    }
    
    
    

def validate_spark_schema_against_postgres(df, postgres_schema: dict) -> None:
    """
    Validates Spark DataFrame schema against expected PostgreSQL schema.

    Raises:
        ValueError if schema is incompatible.
    """

    spark_schema = {field.name: field.dataType for field in df.schema.fields}

    # 1. Missing columns
    missing_cols = postgres_schema.keys() - spark_schema.keys()
    if missing_cols:
        raise ValueError(f"Missing required columns for Postgres: {missing_cols}")

    # 2. Extra columns (optional strictness)
    extra_cols = spark_schema.keys() - postgres_schema.keys()
    if extra_cols:
        raise ValueError(f"Unexpected extra columns for Postgres: {extra_cols}")

    # 3. Type compatibility check
    for col, expected_type in postgres_schema.items():
        actual_type = spark_schema[col]
        if actual_type != expected_type:
            raise ValueError(
                f"Type mismatch for column '{col}': "
                f"expected {expected_type}, got {actual_type}"
            )
