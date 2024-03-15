import sys
import os
import psycopg2
import pandas as pd

# Add the parent directory to the Python path to access db_connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import create_connection directly from db_connection.py
from db_connection import create_connection, close_connection

def create_tables(filename, conn):
    try:
        # Create a cursor to execute SQL commands
        cur = conn.cursor()

        # Read the SQL script
        with open(filename, 'r') as file:
            sql_script = file.read()

        # Execute the SQL commands
        cur.execute(sql_script)

        # Commit the transaction
        conn.commit()
        print("Script executed successfully!")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor
        if cur:
            cur.close()

def execute_sql_scripts(file_paths, conn):
    try:
        # Open a cursor to execute SQL commands
        cur = conn.cursor()

        for file_path in file_paths:
            # Read the SQL script
            with open(file_path, 'r') as file:
                sql_script = file.read()

            # Execute the SQL commands
            cur.execute(sql_script)

            # Commit the transaction
            conn.commit()
            print(f"Script '{file_path}' executed successfully!")

    except psycopg2.Error as e:
        # Rollback the transaction on error
        conn.rollback()
        print(f"Error: {e}")

    finally:
        # Close the cursor
        if cur:
            cur.close()

def read_data_to_dataframe(query, conn):
    try:
        # Use Pandas to read SQL query result into DataFrame
        df = pd.read_sql_query(query, conn)
        return df

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    try:
 # Database connection parameters
        db_name = "source_db"
        db_user = "postgres"
        db_password = "root"
        db_host = "localhost"
        db_port = "5432"

        # Connect to the PostgreSQL database
        conn = create_connection(db_name, db_user, db_password, db_host, db_port)

        # Execute the SQL script to create schema and tables
        create_tables("stg/stg_create_table.sql", conn)

        # List of file paths for SQL scripts
        file_paths = [
            "stg/stg_product.sql",
            "stg/stg_country.sql",
            "stg/stg_date.sql",
            "stg/stg_segment.sql",
            "stg/stg_discountband.sql",
            "stg/stg_sales.sql"
        ]

        # Execute the SQL scripts
        execute_sql_scripts(file_paths, conn)

        # Read data into DataFrames
        table_queries = {
            "stg_product": "SELECT * FROM stg.stgproduct",
            "stg_country": "SELECT * FROM stg.stgcountry",
            "stg_date": "SELECT * FROM stg.stgdate",
            "stg_segment": "SELECT * FROM stg.stgsegment",
            "stg_discountband": "SELECT * FROM stg.stgdiscountband",
            "stg_sales": "SELECT * FROM stg.stgsales"
        }

        for table, query in table_queries.items():
            df = read_data_to_dataframe(query, conn)
            if df is not None:
                print(f"{table} Data read successfully:")
                print(df.head())

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        close_connection(conn)
        
