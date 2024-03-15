# db_connection.py
import psycopg2

def create_connection(db_name, db_user, db_password, db_host, db_port):
    """Create a connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connection to PostgreSQL database successful")
        return connection
    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return None

def close_connection(connection):
    """Close the connection to the PostgreSQL database."""
    if connection:
        connection.close()
        print("Connection to PostgreSQL database closed")

def create_database(connection, db_name):
    """Create a new PostgreSQL database."""
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Create the new database
        cursor.execute(f"CREATE DATABASE {db_name}")

        # Close cursor
        cursor.close()

        print(f"Database '{db_name}' created successfully")
    except Exception as e:
        print("Error creating PostgreSQL database:", e)

def create_schema(connection, schema_name):
    """Create a new schema in the PostgreSQL database."""
    try:
        # Create a cursor object
        cursor = connection.cursor()

        # Create the new schema
        cursor.execute(f"CREATE SCHEMA {schema_name}")

        # Close cursor
        cursor.close()

        print(f"Schema '{schema_name}' created successfully")
    except Exception as e:
        print("Error creating PostgreSQL schema:", e)

if __name__ == "__main__":
    # Example usage:
    db_name = "postgres"
    db_user = "postgres"
    db_password = "root"
    db_host = "localhost"
    db_port = "5432"

    connection = create_connection(db_name, db_user, db_password, db_host, db_port)

    # Perform database operations here

    close_connection(connection)
