import mysql.connector
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def get_connection():
    return mysql.connector.connect(
        host ="localhost",
        user = "root",
        password = "Gnilyiwguoy@14",
        database = "fragrance_db"
    )

def load_fragrances():
    conn = get_connection()
    query = "SELECT name, brand, concentration, notes, image_path, retail_price, size_ml, season FROM fragrances;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df