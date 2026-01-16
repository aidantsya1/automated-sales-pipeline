import psycopg2

try:
    conn = psycopg2.connect(
        user="postgres",
        password="pass123",
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )
    cursor = conn.cursor()

    # 2. Sediakan arahan SQL COPY
    # Kita nak ambil data dari VIEW yang kita buat tadi
    query = "SELECT * FROM v_customer_summary WHERE customer_status = 'VIP'"
    output_file = "senarai_vip.csv"

    # 3. Gunakan copy_expert untuk export terus ke CSV
    # Kita tambah HEADER supaya ada tajuk kolum kat atas
    sql_export = f"COPY ({query}) TO STDOUT WITH CSV HEADER"
    
    with open(output_file, "w") as f:
        cursor.copy_expert(sql_export, f)

    print(f"Selesai! Fail '{output_file}' telah berjaya dicipta.")

except Exception as e:
    print(f"Alamak, error: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()