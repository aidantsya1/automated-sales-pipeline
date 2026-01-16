import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
conn= None 

try:
    # 1. Bina sambungan ke database dalam Docker
    connection = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME")
    )

    # 2. Buat objek kursor untuk jalankan SQL
    cursor = connection.cursor()
    
    # 3. Tanya database pasal version dia
    cursor.execute("SELECT version();")
    record = cursor.fetchone()

    print(f"You are connected to - {record}")

except Exception as error:
    print(f"Error while connecting to PostgreSQL: {error}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")