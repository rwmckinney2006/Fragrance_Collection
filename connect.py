import mysql.connector
import pandas as pd
\
conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Gnilyiwguoy@14",
    database = "fragrance_db"
)

table_name = "fragrances"

df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

df.to_csv("fragrances.csv", index=False)

conn.close()

print("Export complete!")
