import pymysql.cursors
import psycopg2

def init_db_mysql(con):
    try:
        con['charset'] = 'utf8mb4'
        con['cursorclass'] = pymysql.cursors.DictCursor
        connection = pymysql.connect(**con)
        print('DB connect')
        return connection
    except Exception as e:
        print(f'error bd connection {e}')

def init_db_postgre(con):
    try:
        connection =  psycopg2.connect(**con)
        print('DB connect')
        return connection
    except Exception as e:
        print(f'error bd connection {e}')

def execute_query(con,query,engine):
    if engine == 'mysql':
        conn = init_db_mysql(con)
    elif engine == 'postgres':
        conn = init_db_postgre(con)
    try:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f'Error Query > {e}')
        return []
        
def create_update_query(con,query,engine):
    print(f'CONN {con} QUERY {query} ENGINE {engine}')
    if engine == 'mysql':
        conn = init_db_mysql(con)
    elif engine == 'postgres':
        conn = init_db_postgre(con)
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return True
    except Exception as e:
        print(f'Error Query > {e}')
        return False

def create_update_query_tbl(con,query,engine):
    print(f'CONN {con} QUERY {query} ENGINE {engine}')
    if engine == 'mysql':
        conn = init_db_mysql(con)
    elif engine == 'postgres':
        conn = init_db_postgre(con)
    try:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        return 1
    except psycopg2.errors.UniqueViolation as e:
        print(f'Error Query > {e}')
        return 3
    except psycopg2.errors.StringDataRightTruncation as e:
        print(f'Error Query > {e}')
        return 2
    except Exception as e:
        print(f'Error Query > {e}')
        return 7