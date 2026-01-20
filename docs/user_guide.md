# User Guide – Real-Time Data Ingestion Project

This guide explains how to run the real-time data ingestion project using Spark Structured Streaming and PostgreSQL.

Follow the steps in order.

---

## 1. Prerequisites

Make sure the following tools are installed on your system:

- Docker
- Docker Compose
- Git
- Python 3.10+ (for running generator locally)
- Web browser (for pgAdmin)

---

## 2. Clone the Project

Clone the repository to your local machine:

bash
git clone (https://github.com/GhGuda/Real-Time-Data-Ingestion-Spark-Postgres-Amalitech)

cd Real-Time-Data-Ingestion-Spark-Postgres


## 3. Environment Variables Setup

Create a .env file in the project root directory and add the following values


POSTGRES_DB=ecommerce_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin123

DATABASE_URL=jdbc:postgresql://postgresql:5432/ecommerce_db?user=postgres&password=postgres



## 4. Start the Services

Run the following command to build and start all services

docker-compose up --build

<!-- 
This will start:

PostgreSQL database

pgAdmin

Spark master and worker

Spark streaming job container -->



## 5. Access pgAdmin

Open a browser and visit
http://localhost:8080


<!-- 
Login using:

Email: admin@example.com

Password: admin123

Connect pgAdmin to PostgreSQL using:

Host: postgresql

Port: 5432

Username: postgres

Password: postgres

Database: ecommerce_db
-->


## 6. Generate Streaming Data

Run the data generator as a module to create CSV files

python -m generator.data_generator

<!--
The script will continuously generate CSV files in the inputs directory.
-->



## 7. Verify Streaming in PostgreSQL

In pgAdmin, run the following SQL query

SELECT * FROM ecommerce_events;


<!--
You should see new rows appearing as CSV files are generated.
-->


## 8. Stop the Project

To stop all running containers

docker-compose down



## 9. Troubleshooting

Ensure Docker is running before starting the project

Ensure the .env file exists and is correctly configured

Check container logs if data is not appearing

docker logs ecommerce_spark_job



## 10. Conclusion

This project runs a complete real-time data ingestion pipeline using Spark Structured Streaming and PostgreSQL.
Following this guide allows users to run, test, and verify the system successfully.