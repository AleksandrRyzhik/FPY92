import psycopg2

def create_table():
    cur.execute("""
        create table clients (
            id int primary key 
            , first_name varchar(50)
            , last_name varchar(50)
            , email varchar(150)
        );
        """)
    conn.commit() #fix db

with psycopg2.connect(database="netology_db"
                      , user="postgres"
                      , password="postgres") \
as conn:
    with conn.cursor() as cur:
        create_table()
conn.close()

    