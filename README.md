Real-Time Data Ingestion with Spark Structured Streaming & PostgreSQL

A containerized real-time data ingestion pipeline that simulates e-commerce events, processes them using Apache Spark Structured Streaming, and persists the data into PostgreSQL.

Project Overview

This project demonstrates how to build a real-time file-based streaming pipeline using Spark Structured Streaming.
It simulates continuous user activity events and ingests them into a relational database with proper handling of streaming semantics, checkpointing, and fault tolerance.

Architecture
Data Generator → CSV Files → Spark Structured Streaming → PostgreSQL


Components

Data Generator: Simulates real-time e-commerce events

Spark Structured Streaming: Processes incoming files in micro-batches

PostgreSQL: Stores ingested events

pgAdmin: Database UI

Docker & Docker Compose: Container orchestration

Tech Stack

Apache Spark 3.5+

PostgreSQL 15

Python 3.10+

Docker & Docker Compose

pgAdmin

Prerequisites

Ensure the following are installed:

Docker

Docker Compose

Git

Python 3.10+

Web browser (for pgAdmin)

Run Locally
Clone the Repository
git clone https://github.com/GhGuda/Real-Time-Data-Ingestion-Spark-Postgres-Amalitech
cd Real-Time-Data-Ingestion-Spark-Postgres-Amalitech

Environment Variables

Create a .env file in the project root and add:

POSTGRES_DB=ecommerce_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin123

DATABASE_URL=jdbc:postgresql://postgresql:5432/ecommerce_db?user=postgres&password=postgres

Start the Services
Build the Containers
docker-compose build

Run the Project
docker-compose up

Run in Background
docker-compose up -d


This starts:

PostgreSQL

pgAdmin

Spark master & worker

Spark Structured Streaming job

Generate Streaming Data

Run the data generator locally:

python -m generator.data_generator


The generator continuously creates CSV files in the data/inputs directory, which Spark automatically ingests.

Access pgAdmin

Open your browser:

http://localhost:8080


Login Credentials

Email: admin@example.com

Password: admin123

PostgreSQL Connection Settings

Host: postgresql

Port: 5432

Username: postgres

Password: postgres

Database: ecommerce_db

Verify Data Ingestion

Run the following query in pgAdmin:

SELECT * FROM ecommerce_events;


You should see new records appearing as streaming data is generated.

Spark UI

Access the Spark Web UI:

http://localhost:8081


Use this to monitor:

Active streaming queries

Micro-batch execution

Input and processed rows

Stop the Project
Stop Containers
docker-compose down

Stop and Remove Volumes (Clean Reset)
docker-compose down -v

Troubleshooting

Ensure Docker is running

Confirm .env file is correctly configured

Check Spark logs if data is not inserting:

docker logs ecommerce_spark_job


Ensure input files are append-only

Clear checkpoints if schemas change