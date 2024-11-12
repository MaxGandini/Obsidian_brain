import psycopg2
import os

from pathlib import Path

grandparent_dir= Path(__file__).parents[2]

# Define the path to the directory containing the dataset (not the file itself)
data_dir = grandparent_dir / "datasets"  # This should be the directory containing Housing.csv

tables=[]
names=[]
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

# Define the SQL COPY command with the file path

for csv_file_path, table_name in zip(tables, names):
    # Ensure the file exists before attempting to load it
    if csv_file_path.exists():
        try:
            cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}""")

            # Dynamically insert the table name and file path into the COPY SQL statement

            copy_sql = f"""
                COPY {table_name}
                FROM '{csv_file_path}'
                WITH CSV HEADER DELIMITER ','
            """

            # Open the file and execute the COPY command
            with open(csv_file_path, 'r') as f:
                cur.copy_expert(sql=copy_sql, file=f)
            conn.commit()
            print(f"Data from {csv_file_path} successfully loaded into {table_name}.")
        except Exception as e:
            print(f"Error loading data from {csv_file_path} into {table_name}: {e}")
            conn.rollback()
    else:
        print(f"File {csv_file_path} does not exist!")

# Don't forget to close the connection when done
cur.close()
conn.close()

