import os
import pandas as pd
import psycopg2
from pathlib import Path

# Get the grandparent directory
grandparent_dir = Path(__file__).parents[2]

# Define the path to the directory containing the dataset (not the file itself)
data_dir = grandparent_dir / "datasets"

csv_files = list(data_dir.glob("*.csv"))
parquet_files = list(data_dir.glob("*.parquet"))

# Combine the lists of files
all_files = csv_files + parquet_files

# Extract the names without extensions
names = [file.name.split('.')[0] for file in all_files]

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

# Function to clean up a table
def clean_table(table_name):
    try:
        cur.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE;")
        print(f"Table {table_name} dropped.")
    except Exception as e:
        print(f"Error dropping table {table_name}: {e}")
        conn.rollback()

# Process each CSV file
for file_path, table_name in zip(all_files, names):
    if file_path.exists():
        try:
            # Read the CSV file with pandas to infer types
            if file_path.suffix == '.csv':
                df = pd.read_csv(file_path)
            else:
                df = pd.read_parquet(file_path)

            # Clean up the table if it exists
            clean_table(table_name)

            # Generate column definitions for table creation
            columns = []
            for col, dtype in df.dtypes.items():
                col_type = map_dtype_to_sql(dtype)
                columns.append(f"{col} {col_type}")

            # Create the table with inferred columns
            create_table_sql = f"""
                CREATE TABLE {table_name} (
                    {', '.join(columns)}
                );
            """
            cur.execute(create_table_sql)
            print(f"Table {table_name} created.")

            # Define the COPY SQL command
            if file_path.suffix == '.csv':
                copy_sql = f"""
                    COPY {table_name}
                    FROM STDIN WITH CSV HEADER DELIMITER ',' QUOTE '"'
                """
            else:
                copy_sql = f"""
                    COPY {table_name}
                    FROM STDIN WITH PARQUET HEADER DELIMITER ',' QUOTE '"'
                """

            with open(file_path, 'r') as f:
                cur.copy_expert(sql=copy_sql, file=f)

            conn.commit()
            print(f"Data from {file_path} successfully loaded into {table_name}.")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            conn.rollback()
    else:
        print(f"File {file_path} does not exist!")

# Close the cursor and connection
cur.close()
conn.close()

