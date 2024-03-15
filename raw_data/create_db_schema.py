# create_db_schema.py
import sys
import os
import time

# Add the parent directory to the Python path to access db_connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import create_connection directly from db_connection.py
from db_connection import create_connection, close_connection

def create_database(connection, db_name):
    """Create a new PostgreSQL database."""
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL statement to create the database
        cursor.execute(f"CREATE DATABASE {db_name}")

        # Close cursor
        cursor.close()

        print(f"Database '{db_name}' created successfully")
    except Exception as e:
        print("Error creating PostgreSQL database:", e)

def create_schema(connection, schema_name):
    """Create a new schema in the PostgreSQL database."""
    try:
        # Create a new cursor object
        cursor = connection.cursor()

        # Execute the SQL statement to create the schema
        cursor.execute(f"CREATE SCHEMA {schema_name}")

        # Close cursor
        cursor.close()

        print(f"Schema '{schema_name}' created successfully")
    except Exception as e:
        print("Error creating PostgreSQL schema:", e)

def main():
    # Database connection parameters
    db_name = "source_db"
    db_user = "postgres"
    db_password = "root"
    db_host = "localhost"  # e.g., "localhost" for local server
    db_port = "5432"  # e.g., "5432" for default PostgreSQL port

    # Create a connection to the PostgreSQL database
    connection = create_connection(db_name="postgres", db_user=db_user, db_password=db_password, db_host=db_host, db_port=db_port)

    try:
        # Set autocommit to True to avoid running CREATE DATABASE inside a transaction
        connection.autocommit = True
        
        # Create the database
        create_database(connection, db_name)

        # Wait for the database creation to complete
        time.sleep(10)

        # Close the current connection
        close_connection(connection)

        # Reconnect to the newly created database
        connection = create_connection(db_name=db_name, db_user=db_user, db_password=db_password, db_host=db_host, db_port=db_port)

        # Create the schema within the database
        schema_name = "sourcedb"
        create_schema(connection, schema_name)

    except Exception as e:
        print("Error:", e)
    finally:
        # Close the database connection
        close_connection(connection)

if __name__ == "__main__":
    main()
