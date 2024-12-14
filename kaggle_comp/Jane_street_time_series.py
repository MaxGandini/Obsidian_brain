import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import psycopg2
import os

dbname = os.getenv("DB_NAME")
dbuser = os.getenv("DB_USER")
dbpassword = os.getenv("DB_PASSWORD")
dbhost = os.getenv("DB_HOST")
dbport = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=dbuser,
        password=dbpassword,
        host=dbhost,
        port=dbport
    )
    
    cursor = conn.cursor()
    
    # Write your query
    query = "SELECT * FROM "
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all rows
    rows = cursor.fetchall()
    
    # Fetch column names
    colnames = [desc[0] for desc in cursor.description]
    
    df = pd.DataFrame(rows, columns=colnames)
    display(df)
    display(df.columns)
    display(df.info())
    display(df.describe(include='all'))

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Connection closed")

