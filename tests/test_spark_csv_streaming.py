import csv
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType


def test_spark_detects_new_csv_file(tmp_path):
    spark = None
    try:
        # ----------------------------------
        # 1. Spark session (local mode)
        # ----------------------------------
        spark = (
            SparkSession.builder
            .master("local[1]")
            .appName("spark-stream-test")
            .config("spark.ui.enabled", "false")
            .getOrCreate()
        )

        spark.sparkContext.setLogLevel("ERROR")

        # ----------------------------------
        # 2. Define schema (NO id)
        # ----------------------------------
        schema = StructType([
            StructField("event", StringType(), True),
            StructField("user_name", StringType(), True),
            StructField("product", StringType(), True),
            StructField("price", DoubleType(), True),
            StructField("event_time", StringType(), True),
        ])

        input_dir = tmp_path / "inputs"
        input_dir.mkdir()

        # ----------------------------------
        # 3. Start streaming read
        # ----------------------------------
        df = (
            spark.readStream
            .schema(schema)
            .option("header", "true")
            .csv(str(input_dir))
        )

        collected = []

        def collect_batch(batch_df, batch_id):
            collected.extend(batch_df.collect())

        query = (
            df.writeStream
            .trigger(once=True)          # 🔑 process once only
            .foreachBatch(collect_batch)
            .start()
        )

        # ----------------------------------
        # 4. Write ONE CSV file
        # ----------------------------------
        csv_path = input_dir / "event_test.csv"
        with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["event", "user_name", "product", "price", "event_time"])
            writer.writerow(
                ["purchase", "Ama", "Laptop", 2500.50, "2026-01-28 20:00:00"]
            )

        # ----------------------------------
        # 5. Wait for Spark to finish
        # ----------------------------------
        query.awaitTermination(10)

        # ----------------------------------
        # 6. Assertions
        # ----------------------------------
        assert len(collected) == 1
        assert collected[0]["event"] == "purchase"

    finally:
        # ----------------------------------
        # 7. GUARANTEED CLEANUP (CRITICAL)
        # ----------------------------------
        if spark:
            for q in spark.streams.active:
                q.stop()
            spark.stop()
