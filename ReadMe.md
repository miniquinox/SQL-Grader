# SQL Assignment Grading System

This document outlines the SQL Assignment Grading System designed for efficiently grading student SQL assignments by comparing their submissions to a set of correct queries provided by the professor. This system aims to automate the grading process, focusing on the accuracy and format of the SQL queries.

## System Overview

The grading system comprises a Python script that reads SQL queries from two files: one containing student submissions and the other the professor's correct answers. The script executes each query against a MySQL database, compares the results, and generates a report indicating the correctness of each query based on row counts and the content of the first 10 rows.

## Prerequisites

Before using the grading system, ensure the following prerequisites are met:

- Python installed on the grading system.
- `pymysql` and `pandas` Python libraries installed.
- Access to the MySQL database with the relevant datasets.
- Student submissions and professor's answer key in separate SQL files.

## File Structure

There are two main types of files:

1. **Student's SQL File (`student_queries.sql`)**: Contains the SQL queries written by the student.
2. **Professor's SQL File (`professor_queries.sql`)**: Contains the correct SQL queries for comparison.

### Sample SQL File Format

#### Professor's SQL File

```sql
-- Query 1: Description of Query 1
SELECT * FROM students;

-- Query 2: Description of Query 2
SELECT AVG(age) FROM students;
```

#### Student's SQL File

```sql
Copy code
-- Query 1: Student's attempt for Query 1
SELECT * FROM students WHERE major = 'Computer Science';

-- Query 2: Student's attempt for Query 2
SELECT SUM(age) / COUNT(*) FROM students;
```

## Python Grading Script

### Script Overview

The Python script `grade_sql.py` performs the following tasks:

- Reads queries from the student and professor SQL files.
- Executes each query against the MySQL database.
- Compares the number of rows and the first 10 rows of each result.
- Outputs the comparison results, highlighting discrepancies.

### Usage

#### Set Up Database Connection
Edit the script to include the correct database connection details.

```python
host = 'your_host'
user = 'your_username'
password = 'your_password'
```

## Run the Script
Execute the script with the paths to the student's and professor's SQL files as arguments.

```python
student_file_path = 'path/to/student_queries.sql'
professor_file_path = 'path/to/professor_queries.sql'
```

## Running the System
Place the student and professor SQL files in the designated directory.
Update the script with the correct file paths and database credentials.
Run the script to execute the queries and compare results.
Review the output for each student's submission.

## Security Considerations
Ensure the script runs with limited database permissions to prevent potential harmful operations in student queries.