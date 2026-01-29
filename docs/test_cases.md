# Test Results – Real-Time Data Ingestion Project

This document presents the results of automated tests executed to validate the correctness and reliability of the Real-Time Data Ingestion pipeline built using Apache Spark Structured Streaming and PostgreSQL.

All tests described below were implemented and executed using `pytest` and Spark in local mode.

---

## Test Case 1: Event Schema Validation  
**Type:** Automated Unit Test  

**Objective:**  
Verify that generated user events strictly conform to the expected event schema.

**Test Coverage:**  
- Valid event schema  
- Missing required fields  
- Extra unexpected fields  
- Incorrect data types  

**Test Method:**  
Pytest unit tests validating event dictionaries against the expected schema.

**Result:**  
All schema validation tests passed successfully. Invalid events were correctly rejected.

**Status:**  
✅ Pass

---

## Test Case 2: CSV File Generation  
**Type:** Automated Unit Test  

**Objective:**  
Verify that event data is correctly written to CSV files.

**Test Coverage:**  
- CSV file creation  
- Correct column headers  
- Correct data row content  

**Test Method:**  
Pytest unit test using a temporary directory and monkeypatched output path.

**Result:**  
CSV files were created successfully with valid headers and data.

**Status:**  
✅ Pass

---

## Test Case 3: Spark Detects New CSV Files  
**Type:** Automated Integration Test (Local Spark)  

**Objective:**  
Verify that Spark Structured Streaming detects and processes newly added CSV files.

**Test Coverage:**  
- Spark reads CSV files from an input directory  
- One micro-batch processes available data  
- Streaming query terminates correctly after processing  

**Test Method:**  
Pytest test using Spark in local mode with `trigger(once=True)` and controlled shutdown.

**Result:**  
Spark successfully detected and processed the CSV file.

**Status:**  
✅ Pass

---

## Test Case 4: Data Transformation Logic  
**Type:** Automated Unit Test (Spark DataFrame)  

**Objective:**  
Verify that data transformations are correctly applied before loading.

**Test Coverage:**  
- Data type casting (e.g., price to float)  
- Column selection and ordering  

**Test Method:**  
Pytest Spark unit test applying transformation logic to a sample DataFrame.

**Result:**  
All transformations were applied correctly and output schema matched expectations.

**Status:**  
✅ Pass

---

## Test Case 5: PostgreSQL Write Logic  
**Type:** Automated Unit Test (Mocked)  

**Objective:**  
Verify that the application attempts to write processed data to PostgreSQL using JDBC.

**Test Coverage:**  
- JDBC write format  
- Append write mode  
- Save operation invocation  

**Test Method:**  
Pytest unit test using mocked Spark DataFrame write operations.

**Result:**  
The PostgreSQL write logic was invoked with the correct configuration.

**Status:**  
✅ Pass

---

## Overall Test Summary

- Total Automated Tests Executed: **5**
- All tests passed successfully
- No end-to-end database ingestion test was performed

---

## Conclusion

The implemented automated tests validate the core logic of the real-time data ingestion pipeline, including schema validation, file generation, Spark ingestion behavior, data transformation, and database write intent.

End-to-end database ingestion testing can be added in future work if required.
