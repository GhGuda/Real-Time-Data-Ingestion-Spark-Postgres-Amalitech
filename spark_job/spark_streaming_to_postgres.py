"""
Spark Structured Streaming job that reads real-time e-commerce events
and writes them to PostgreSQL using foreachBatch.
"""

import os, sys
import logging
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, 
    IntegerType, DoubleType)
from pyspark.sql.functions import col, to_timestamp

from configs.logger_config import setup_logger
setup_logger()

# -------------------------------------------------------------------
# Logging
# -------------------------------------------------------------------
setup_logger()
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# Schema Definition
# -------------------------------------------------------------------
event_schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("event", StringType(), True),
    StructField("user_name", StringType(), True),
    StructField("product", StringType(), True),
    StructField("price", DoubleType(), True),
    StructField("event_time", StringType(), True)
])


# ------------------------------------------------------------------
# PostgreSQL config
# ------------------------------------------------------------------
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    logger.error("DATABASE_URL environment variable is not set!")
    sys.exit(1)

logger.info(f"PostgreSQL connection URL: {DATABASE_URL}")

POSTGRES_PROPERTIES = {
    "driver": "org.postgresql.Driver"
}


# ------------------------------------------------------------------
# Write batch to PostgreSQL
# ------------------------------------------------------------------
def write_to_postgres(batch_df, batch_id):
    """
    Writes a micro-batch DataFrame to PostgreSQL.
    """
    try:
        record_count = batch_df.count()
        if record_count == 0:
            logger.info(f"Batch {batch_id} is empty, skipping")
            return

        logger.info(f"Writing batch {batch_id} with {record_count} records to PostgreSQL")

        
        (batch_df.write
            .format("jdbc")
            .option("url", DATABASE_URL)
            .option("dbtable", "ecommerce_events")
            .option("driver", "org.postgresql.Driver")
            .mode("append")
            .save()
        )
        
        logger.info(f"Successfully wrote batch {batch_id} to PostgreSQL")
    except Exception as e:
        logger.error(f"Failed to write batch {batch_id}", exc_info=True)
        
        

# ------------------------------------------------------------------
# Main streaming logic
# ------------------------------------------------------------------
def main() -> None:
    try:
        # -------------------------------------------------------------------
        # Spark Session
        # -------------------------------------------------------------------
        spark = (
            SparkSession.builder
            .appName("SparkToPostgresStreaming")
            .config("spark.jars.packages", "org.postgresql:postgresql:42.7.1")
            .getOrCreate()
        )
        logger.info("Spark session started")
        logger.info(f"Spark version: {spark.version}")

        # -------------------------------------------------------------------
        # Read Streaming Data
        # -------------------------------------------------------------------
        input_df =(
            spark.readStream
            .schema(event_schema)
            .option("header", "true")
            .option("maxFilesPerTrigger", 1)
            .csv("/app/data/inputs")
        )


        # -------------------------------------------------------------------
        # Transform Streaming Data
        # -------------------------------------------------------------------
        transformed_df = (
            input_df
            .withColumn("event_time", to_timestamp(col("event_time")))
        )

        
        checkpoint_path = "/app/data/checkpoints"
        logger.info(f"Checkpoint location: {checkpoint_path}")
        
        # -------------------------------------------------------------------
        # Output Stream
        # -------------------------------------------------------------------
        query = (
            transformed_df.writeStream
            .foreachBatch(write_to_postgres)
            .outputMode("append")
            .option("checkpointLocation", checkpoint_path)
            .option("failOnDataLoss", "false")
            .start()
        )


        logger.info("Streaming query started successfully")
        logger.info("Waiting for data...")
        query.awaitTermination()
 
    except Exception as e:
        logging.error(f"Failed to read streaming data: {e}", exc_info=True)
        spark.stop()
        raise

if __name__ == "__main__":
    main()
