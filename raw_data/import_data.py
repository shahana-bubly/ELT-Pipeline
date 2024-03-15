import sys
import os
import pandas as pd
import psycopg2

# Add the parent directory to the Python path to access db_connection.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import create_connection directly from db_connection.py
from db_connection import create_connection, close_connection

# Path to the Excel file
file_path = "raw_data/files/Financial Sample.xlsx"

# Read Excel file into a Pandas DataFrame
df = pd.read_excel(file_path)

# Database connection parameters
db_name = "source_db"
db_user = "postgres"
db_password = "root"
db_host = "localhost"
db_port = "5432"
schema_name = "sourcedb"
table_name = "financialData"

# Connect to the PostgreSQL server
connection = create_connection(db_name, db_user, db_password, db_host, db_port)

# Read SQL script from file and execute to create table
with open('raw_data/create_table.sql', 'r') as file:
    create_table_query = file.read()

# Create a cursor object
cursor = connection.cursor()

# Execute the SQL script to create the table
cursor.execute(create_table_query)

# Commit the transaction
connection.commit()

# Close cursor
cursor.close()

# Now, insert data from the DataFrame into the PostgreSQL table
try:
    # Connect to the PostgreSQL server
    connection = create_connection(db_name, db_user, db_password, db_host, db_port)

    # Create a cursor object
    cursor = connection.cursor()

    # Insert data into PostgreSQL table
    for index, row in df.iterrows():
        cursor.execute(
            f"INSERT INTO {schema_name}.{table_name} VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            tuple(row)
        )

    # Commit the transaction
    connection.commit()

    print("Data inserted successfully")
except Exception as e:
    print("Error inserting data:", e)
finally:
    # Close cursor and connection
    cursor.close()
    connection.close()
