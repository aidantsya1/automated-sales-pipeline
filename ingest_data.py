import psycopg2
from faker import Faker
import random
import os
from dotenv import load_dotenv

load_dotenv()
conn = None
# 1. Setup Faker
fake = Faker()
try:
    conn = psycopg2.connect(
       user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()

    print("Mula masukkan data...")

    # 3. Masukkan 50 Customers secara rawak
    for _ in range(50):
        name = fake.name()
        city = fake.city()
        cursor.execute("INSERT INTO customers (name, city) VALUES (%s, %s)", (name, city))

    # 4. Masukkan 100 Orders secara rawak
    # Kita guna id dari 1-50 sebab kita tahu kita ada 50 customers tadi
    products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphone']
    
    for _ in range(100):
        c_id = random.randint(1, 50)
        prod = random.choice(products)
        price = round(random.uniform(50.0, 5000.0), 2)
        cursor.execute(
            "INSERT INTO orders (customer_id, product, price) VALUES (%s, %s, %s)", 
            (c_id, prod, price)
        )
        #    "INSERT INTO orders (customer_id, product, price) VALUES (1,'Barang Rosak', -100.00)")

    # 5. Save (Commit) perubahan
    conn.commit()
    print("Selesai! 150 rekod berjaya dimasukkan.")

except Exception as e:
    print(f"Alamak, error: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()