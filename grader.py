import pymysql
import pandas as pd

# Database connection details
host = 'localhost'
user = 'root'
password = 'your_password'

def read_queries_from_file(file_path):
    with open(file_path, 'r') as file:
        # Splitting the file content by ';' to get individual queries
        queries = file.read().split(';')
        queries = [q.strip() for q in queries if q.strip()]
    return queries

def execute_query(query, connection):
    try:
        # Handling the USE statement
        if query.lower().startswith('use '):
            with connection.cursor() as cursor:
                cursor.execute(query)
            return pd.DataFrame(), None  # No data to return for USE statement
        else:
            return pd.read_sql(query, connection), None
    except Exception as e:
        return None, str(e)

def compare_queries(student_queries, professor_queries, connection):
    for i, (student_query, professor_query) in enumerate(zip(student_queries, professor_queries)):
        student_result, student_error = execute_query(student_query, connection)
        professor_result, professor_error = execute_query(professor_query, connection)

        if student_error or professor_error:
            print(f"Error in Query {i+1}: Student Error: {student_error}, Professor Error: {professor_error}")
            continue

        same_row_count = len(student_result) == len(professor_result)
        same_first_10_rows = student_result.head(10).equals(professor_result.head(10))

        print(f"Query {i+1}: Same Row Count: {same_row_count}, Same First 10 Rows: {same_first_10_rows}")

# Main Execution
connection = pymysql.connect(host=host, user=user, password=password)

student_file_path = 'path/to/student_queries.sql'
professor_file_path = 'path/to/professor_queries.sql'

student_queries = read_queries_from_file(student_file_path)
professor_queries = read_queries_from_file(professor_file_path)

compare_queries(student_queries, professor_queries, connection)

connection.close()