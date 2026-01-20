# Real-Time Data Ingestion Using Spark Structured Streaming & PostgreSQL

## Project Overview

This project demonstrates a real-time data ingestion pipeline that simulates an e-commerce platform tracking user activity such as product views and purchases.

Fake e-commerce events are continuously generated, processed in real time using Apache Spark Structured Streaming, and stored in a PostgreSQL database for analysis and verification.

The goal of this project is to show how streaming data can be ingested, transformed, and persisted using modern data engineering tools.

---

## System Components

The system is made up of the following components:

### 1. Data Generator
A Python script generates fake e-commerce events in CSV format.  
Each event contains information such as:
- event type (view or purchase)
- user name
- product name
- price
- event timestamp  

The generated CSV files are saved continuously into an inputs folder.

---

### 2. Spark Structured Streaming
Apache Spark Structured Streaming monitors the inputs folder for new CSV files.

As new files appear:
- Spark reads them as a streaming source
- Applies basic transformations such as type conversion
- Prepares the data for storage

Spark processes the data in micro-batches, enabling near real-time ingestion.

---

### 3. PostgreSQL Database
PostgreSQL is used as the storage layer for processed events.

Spark writes each processed micro-batch into a relational table called `ecommerce_events`.  
This allows the streamed data to be queried, verified, and analyzed using SQL.

---

## Data Flow

The data flows through the system in the following order:

1. Python script generates e-commerce event data as CSV files  
2. Spark Structured Streaming detects new files in the inputs directory  
3. Spark processes and transforms the data in real time  
4. Processed data is written into PostgreSQL  
5. Data can be viewed and verified using pgAdmin or SQL queries  

---

## Technologies Used

- Python (data generation)
- Apache Spark Structured Streaming (real-time processing)
- PostgreSQL (data storage)
- SQL (database setup and querying)
- Docker & Docker Compose (containerized environment)

---

## Conclusion

This project demonstrates a complete real-time data pipeline, from event generation to persistent storage.  
It highlights how Spark Structured Streaming can be used to handle continuously arriving data and integrate with a relational database like PostgreSQL.
