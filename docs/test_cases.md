# Test Cases – Real-Time Data Ingestion Project

This document describes the manual test cases performed to verify the functionality of the real-time data ingestion pipeline.

---

## Test Case 1: CSV File Generation

**Objective:**  
Verify that the data generator creates CSV files correctly.

**Steps:**
1. Run the data generator script.
2. Observe the inputs directory for new CSV files.

**Expected Result:**  
New CSV files are created at intervals of 3 seconds.

**Actual Result:**  
CSV files were successfully generated.

**Status:**  
✅ Pass

---

## Test Case 2: Spark Detects New CSV Files

**Objective:**  
Verify that Spark Structured Streaming detects newly added CSV files.

**Steps:**
1. Start all Docker services.
2. Run the data generator.
3. Monitor Spark logs.

**Expected Result:**  
Spark detects and processes new CSV files automatically.

**Actual Result:**  
Spark successfully detected and processed new files.

**Status:**  
✅ Pass

---

## Test Case 3: Data Schema Validation

**Objective:**  
Verify that incoming CSV data matches the defined Spark schema.

**Steps:**
1. Check the Spark schema configuration.
2. Compare with CSV column structure.

**Expected Result:**  
CSV columns match the defined schema without errors.

**Actual Result:**  
Schema matched successfully.

**Status:**  
✅ Pass

---

## Test Case 4: Data Transformation

**Objective:**  
Verify that data transformations (type conversion, column renaming) are applied correctly.

**Steps:**
1. Inspect Spark transformation logic.
2. Check resulting data written to PostgreSQL.

**Expected Result:**  
Fields are properly transformed (e.g., timestamps converted correctly).

**Actual Result:**  
Transformations applied successfully.

**Status:**  
✅ Pass

---

## Test Case 5: Write Data to PostgreSQL

**Objective:**  
Verify that processed streaming data is written into PostgreSQL.

**Steps:**
1. Open pgAdmin.
2. Run a SELECT query on the target table.

**Expected Result:**  
New records appear in the database as streaming continues.

**Actual Result:**  
Data was written successfully into PostgreSQL.

**Status:**  
✅ Pass

---

## Test Case 6: Continuous Streaming

**Objective:**  
Verify that the system continuously processes incoming data.

**Steps:**
1. Keep the generator running.
2. Monitor PostgreSQL table updates.

**Expected Result:**  
Database table updates continuously without stopping.

**Actual Result:**  
Streaming pipeline ran continuously as expected.

**Status:**  
✅ Pass

---

## Test Case 7: Error Handling

**Objective:**  
Verify system behavior when no new files are available.

**Steps:**
1. Stop the data generator.
2. Observe Spark logs.

**Expected Result:**  
Spark continues running without crashing.

**Actual Result:**  
Spark remained active and stable.

**Status:**  
✅ Pass

---

## Conclusion

All test cases passed successfully.  
The system meets the functional requirements for real-time data ingestion using Spark Structured Streaming and PostgreSQL.
