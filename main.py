import pyodbc
import os
from dotenv import load_dotenv
load_dotenv(".env")


def create_connection_string():
    # Read connection parameters from environment variables
    server = os.environ.get('SQL_SERVER')
    username = os.environ.get('SQL_USERNAME')
    password = os.environ.get('SQL_PASSWORD')
    port = os.environ.get('SQL_PORT')
    database = os.environ.get('SQL_DATABASE')

    if not (server and username and password and port and database):
        raise ValueError("Missing one or more required environment variables")

    # Construct the connection string
    conn_str = (
        f'Driver={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'PORT={port};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password};'
    )

    return conn_str


def execute_sql_query(query):
    try:
        conn_str = create_connection_string()
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()

        print('Using the following SQL Server version:')
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        print("columns", columns)

        for row in cursor.fetchall():
            print(row)
            items = dict(zip(columns, row))

    except pyodbc.Error as e:
        print(f"Error executing SQL query: {e}")


if __name__ == "__main__":
    # Example usage:
    sql_query = os.getenv("SQL_QUERY", "null")
    print("sql_query")
    print(sql_query, end="\n")
    execute_sql_query(sql_query)
