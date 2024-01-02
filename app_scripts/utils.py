import psycopg2
import os

def db_connect():
    conn = psycopg2.connect(
       dbname=os.environ.get('POSTGRES_DB'),
       user=os.environ.get('POSTGRES_USER'),
       password=os.environ.get('POSTGRES_PASSWORD'),
       host=os.environ.get('POSTGRES_HOST'),
       port=os.environ.get('POSTGRES_PORT')
       )
    
    cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.close()
    cur.close()
    return

def create_table(table_name, columns):
    try:
        conn, cur = db_connect()
    except:
        print("Error connecting to database")
        return
    
    cur.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns});")

    conn.commit()

    db_close(conn, cur)

    print(f"Table {table_name} created successfully")

    return

def drop_table(table_name):
    try:
        conn, cur = db_connect()
    except:
        print("Error connecting to database")
        return
    
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")

    conn.commit()

    db_close(conn, cur)

    print(f"Table {table_name} dropped successfully")

    return

def insert_row(table_name, columns, values):
    try:
        conn, cur = db_connect()
    except:
        print("Error connecting to database")
        return
    
    cur.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values});")

    conn.commit()

    db_close(conn, cur)

    print(f"Row inserted successfully")

    return

def fetch_all(table_name):
    try:
        conn, cur = db_connect()
    except:
        print("Error connecting to database")
        return
    
    cur.execute(f"SELECT * FROM {table_name};")

    result = cur.fetchall()

    db_close(conn, cur)

    print(f"fetchall result: {result}")

    return result

def fetch_one(table_name, column, value):
    try:
        conn, cur = db_connect()
    except:
        print("Error connecting to database")
        return
    
    cur.execute(f"SELECT * FROM {table_name} WHERE {column} = '{value}';")

    result = cur.fetchone()

    db_close(conn, cur)

    print(f"fetchone result: {result}")

    return



    