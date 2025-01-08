import psycopg2

# Configurare conexiune
db_params = {
    'dbname': 'states_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()



    insert_query = '''
        INSERT INTO states (name, area, neighbors, timezone, density, population, lang, political_system, capital)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor.executemany(insert_query, --add data here--)
    conn.commit()

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")
