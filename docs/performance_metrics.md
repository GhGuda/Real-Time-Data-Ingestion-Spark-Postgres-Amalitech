# Performance Metrics – Real-Time Data Ingestion Project

This document reports the observed performance of the real-time data ingestion system using Spark Structured Streaming and PostgreSQL.

---

## 1. Test Environment

- **Streaming Engine:** Apache Spark Structured Streaming
- **Database:** PostgreSQL
- **Data Format:** CSV
- **Execution Mode:** Docker containers
- **Data Generation Rate:** Periodic CSV file generation

---

## 2. Metrics Observed

### 2.1 Latency

**Definition:**  
Latency is the time taken for a generated CSV file to be processed by Spark and written into PostgreSQL.

**Observation Method:**  
- Time when CSV file is generated
- Time when record appears in PostgreSQL

**Observed Latency:**  
Approximately **3-7 seconds** per file.

**Remarks:**  
Latency remained stable during continuous streaming.

---

### 2.2 Throughput

**Definition:**  
Throughput is the number of records processed by the system per unit time.

**Observation Method:**  
- Count records inserted into PostgreSQL over time
- Monitor Spark logs

**Observed Throughput:**  
- Approximately **15–20 records per minute** (depending on generation rate)

**Remarks:**  
System handled incoming data without backlog.

---

### 2.3 System Stability

**Definition:**  
Stability refers to the system’s ability to run continuously without crashing.

**Observation Method:**  
- Monitor Docker container status
- Observe Spark logs

**Observed Behavior:**  
- Spark streaming job remained active
- No manual restart required during testing

**Remarks:**  
System was stable under normal load.

---

## 3. Resource Usage (Basic Observation)

- **CPU Usage:** Moderate
- **Memory Usage:** Stable
- **Disk Usage:** Increased gradually as data accumulated

No abnormal resource consumption was observed.

---

## 4. Performance Summary

| Metric      | Observation            |
|------------|------------------------|
| Latency    | 3–7 seconds            |
| Throughput | 15–20 records/minute   |
| Stability  | Stable                 |

---

## 5. Conclusion

The real-time data ingestion pipeline performed reliably under test conditions.  
Spark Structured Streaming successfully processed incoming CSV files and stored them in PostgreSQL with low latency and consistent throughput.
