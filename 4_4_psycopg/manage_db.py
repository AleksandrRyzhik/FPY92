import psycopg2    

def create_tables():
    '''delete and create tables clients and 
    phones_clients'''
    
    cur.execute("""
    drop table if exists phones_clients;
    drop table if exists clients;
                
    create table clients (
        id serial primary key 
        , first_name varchar(50)
        , last_name varchar(50)
        , email varchar(150)
    );
    create table phones_clients(
        id_client int references clients(id)
        , phone varchar (16)
    );
    """)
    
def add_client(fname, lname
                , email):
    cur.execute("""
    insert into clients(first_name
                , last_name, email)
                values(%s, %s, %s);
    """
    , (fname, lname, email) )

def add_phone(client_id, phone):
    cur.execute("""
    insert into phones_clients(id_client, phone)
               values(%s, %s)
                returning id_client; 
    """, (client_id, phone))
    print('id_client_with_phone', cur.fetchone())

def upd_client_info(client_id, fname, lname
                    , email):
    cur.execute("""
    update clients set first_name=%s
                , last_name=%s, email=%s
                where id=%s
    """, (fname, lname, email, client_id))
    cur.execute("""
    select * from clients where id=%s
    """, (client_id,))
    print('new_info_client:', cur.fetchall())

def del_phone(id_client):
    cur.execute("""
    update phones_clients
                set phone = null
                where id_client=%s
    """, (id_client,))
    cur.execute("""
    select * from phones_clients
                where id_client=%s
    """, (id_client,))
    print('client_id_and_phone:', cur.fetchall())

def del_client(id_client):
    cur.execute("""
    delete from phones_clients
                where id_client=%s
    """, (id_client,))
    cur.execute("""
    delete from clients
                where id=%s
    """, (id_client,))
    cur.execute("""
    select * from clients
    """)
    print('all_clients_now:', cur.fetchall())

def find_client(fname='%', lname='%'
                , email='%', phone='%'):
    cur.execute("""
    select c.* 
    from clients c
        left join 
            phones_clients pc
                on c.id=pc.id_client
    where c.first_name like %s and
                c.last_name like %s
                and c.email like %s
                and pc.phone like %s
    """, (fname, lname, email, phone))
    print('finded client:', cur.fetchall())
    
    

with psycopg2.connect(database="netology_db"
                      , user="postgres"
                      , password="postgres") \
                        as conn:
    with conn.cursor() as cur:
        create_tables()
        add_client('sasha', 'cockney'
                   , 'sc@d.com')
        add_phone(1, '+7 934 893 66 55')
        upd_client_info(1, 'evgeny', 'sokolov'
                        , 'es@m.ru')
        find_client(phone=
                    '+7 934 893 66 55')
        del_phone(1)
        del_client(1)
conn.close()