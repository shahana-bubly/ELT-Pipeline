# create_schema.py
import sys
import os
import time

# Add the parent directory to the Python path to access db_connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import create_connection directly from db_connection.py
from db_connection import create_connection, close_connection
def create_schema(db_name, db_user, db_password, db_host, db_port, schema_name):
    try:
        # Connect to the PostgreSQL server
        connection = create_connection(db_name, db_user, db_password, db_host, db_port)
        connection.autocommit = True  # Ensure that commands are executed immediately

        # Create a cursor object
        cursor = connection.cursor()
        
        # Execute SQL statement to create the schema
        cursor.execute(f"CREATE SCHEMA {schema_name}")

        # Close cursor and connection
        cursor.close()
        close_connection(connection)

        print(f"Schema '{schema_name}' created successfully")
    except Exception as e:
        print("Error creating schema:", e)

if __name__ == "__main__":
    # Database connection parameters
    db_name = "source_db"
    db_user = "postgres"
    db_password = "root"
    db_host = "localhost"  # e.g., "localhost" for local server
    db_port = "5432"  # e.g., "5432" for default PostgreSQL port

    # Schema name to create
    schema_name = "sourcedb"

    # Create the schema
    create_schema(db_name, db_user, db_password, db_host, db_port, schema_name)
