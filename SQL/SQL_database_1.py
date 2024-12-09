import os
import csv
import pandas as pd
import psycopg2
from pathlib import Path

# Get the grandparent directory
grandparent_dir = Path(__file__).parents[2]

# Define the path to the directory containing the dataset (not the file itself)
data_dir = grandparent_dir / "datasets"  # This should be the directory containing Housing.csv

tables = []
names = []

# Check if the directory exists and then list its contents
if data_dir.exists() and data_dir.is_dir():
    for archive in data_dir.iterdir():
        print(archive)
        tables.append(archive)
else:
    print(f"{data_dir} is not a valid directory.")

csv_files = list(data_dir.glob("*.csv"))

# Print out each CSV file name
for csv_file in csv_files:
    print(csv_file.name)  # This will print just the file name, not the full path
    names.append(csv_file.name.split('.')[0])

# Access environment variables
dbname = os.getenv("DB_NAME")
dbuser = os.getenv("DB_USER")
dbpassword = os.getenv("DB_PASSWORD")
dbhost = os.getenv("DB_HOST")
dbport = os.getenv("DB_PORT")

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=dbname,
    user=dbuser,
    password=dbpassword,
    host=dbhost,
    port=dbport
)

# Create a cursor to execute SQL commands
cur = conn.cursor()

# Function to map pandas data types to PostgreSQL types
def map_dtype_to_sql(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return 'INTEGER'
    elif pd.api.types.is_float_dtype(dtype):
        return 'FLOAT'
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return 'TIMESTAMP'
    elif pd.api.types.is_bool_dtype(dtype):
        return 'BOOLEAN'
    else:
        return 'TEXT'

# Define the SQL COPY command with the file path
for csv_file_path, table_name in zip(csv_files, names):
    # Ensure the file exists before attempting to load it
    if csv_file_path.exists():
        try:
            # Read the CSV file with pandas to infer types
            df = pd.read_csv(csv_file_path)
            
            # Generate column definitions for table creation
            columns = []
            for col, dtype in df.dtypes.items():
                col_type = map_dtype_to_sql(dtype)
                columns.append(f"{col} {col_type}")
            
            # Create the table with inferred columns
            create_table_sql = f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    {', '.join(columns)}
                )
            """
            cur.execute(create_table_sql)
            print(f"Table {table_name} created or already exists.")

            # Define the COPY SQL command
            copy_sql = f"""
                COPY {table_name}
                FROM STDIN WITH CSV HEADER DELIMITER ',' QUOTE '\"'
            """
            with open(csv_file_path, 'r') as f:
                cur.copy_expert(sql=copy_sql, file=f)
            
            conn.commit()
            print(f"Data from {csv_file_path} successfully loaded into {table_name}.")
        except Exception as e:
            print(f"Error loading data from {csv_file_path} into {table_name}: {e}")
            conn.rollback()
    else:
        print(f"File {csv_file_path} does not exist!")

# Close the cursor and connection
cur.close()
conn.close()
