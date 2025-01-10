import psycopg2
from psycopg2 import sql

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

DB_NAME = 'states_db'

try:
    conn = psycopg2.connect(**db_params)
    conn.autocommit = True
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'"
    )
    if not cursor.fetchone():
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(DB_NAME)
        ))
        print(f"Database '{DB_NAME}' created successfully.")
    else:
        print(f"Database '{DB_NAME}' already exists.")

    cursor.close()
    conn.close()

    db_params['dbname'] = f'{DB_NAME}'
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS states (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            area INTEGER,
            neighbors TEXT,
            timezone VARCHAR(50),
            density FLOAT,
            population BIGINT,
            lang VARCHAR(100),
            political_system VARCHAR(100),
            capital VARCHAR(100)
        );
    ''')
    print("Successfully created table.")

    cursor.close()
    conn.commit()
    conn.close()

except Exception as e:
    print(f"Error: {e}")
