
# Real-Time Data Ingestion with Spark Structured Streaming & PostgreSQL

A containerized real-time data ingestion pipeline that simulates e-commerce events, processes them using Apache Spark Structured Streaming, and persists the data into PostgreSQL.


## Project Overview

This project demonstrates how to build a real-time file-based streaming pipeline using Spark Structured Streaming.
It simulates continuous user activity events and ingests them into a relational database with proper handling of streaming semantics, checkpointing, and fault tolerance.

### Architecture Overview
Data Generator → CSV Files → Spark Structured Streaming → PostgreSQL


### Components

Data Generator: Simulates real-time e-commerce events

Spark Structured Streaming: Processes incoming files in micro-batches

PostgreSQL: Stores ingested events

pgAdmin: Database UI

### Docker & Docker Compose: Container orchestration

Tech Stack

Apache Spark 3.5+

PostgreSQL 15

Python 3.10+

Docker & Docker Compose

pgAdmin

### Prerequisites

Ensure the following are installed:

Docker

Docker Compose

Git

Python 3.10+

Web browser (for pgAdmin)

# Run Locally
Clone the Repository
```bash
git clone https://github.com/GhGuda/Real-Time-Data-Ingestion-Spark-Postgres-Amalitech
```

### Change directory to Real-Time-Data-Ingestion-Spark-Postgres-Amalitech

```bash
cd Real-Time-Data-Ingestion-Spark-Postgres-Amalitech
```
### Environment Variables

Create a .env file in the project root and add:

```bash
POSTGRES_DB=ecommerce_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin123

DATABASE_URL=jdbc:postgresql://postgresql:5432/ecommerce_db?user=postgres&password=postgres
```

### Start the Services
Build the Containers
```bash
docker-compose build
```

Run the Project

```bash
docker-compose up
```

Run in Background

```bash
docker-compose up -d
```

### This starts:

PostgreSQL

pgAdmin

Spark master & worker

Spark Structured Streaming job

### Generate Streaming Data

Run the data generator locally:

```bash
python -m generator.data_generator
```

The generator continuously creates CSV files in the data/inputs directory, which Spark automatically ingests.

### Access pgAdmin

Open your browser:

```bash
http://localhost:8080
```

### Login Credentials

```bash
Email: admin@example.com

Password: admin123

PostgreSQL Connection Settings

Host: postgresql

Port: 5432

Username: postgres

Password: postgres

Database: ecommerce_db
```

### Verify Data Ingestion

Run the following query in pgAdmin:

```bash
SELECT * FROM ecommerce_events;
```

You should see new records appearing as streaming data is generated.

### Spark UI

Access the Spark Web UI:

```bash
http://localhost:8081
```

### Use this to monitor:

Active streaming queries

Micro-batch execution

Input and processed rows

### Stop the Project
Stop Containers

```bash
docker-compose down
```

### Stop and Remove Volumes (Clean Reset)

```bash
docker-compose down -v
```

### Troubleshooting

Ensure Docker is running

Confirm .env file is correctly configured

Check Spark logs if data is not inserting:

```bash
docker logs ecommerce_spark_job
```

Ensure input files are append-only

Clear checkpoints if schemas change