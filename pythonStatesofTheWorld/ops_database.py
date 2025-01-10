import psycopg2

# Configurare conexiune
db_params = {
    'dbname': 'states_db',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

def insert_state_data(state_name, state_data_dict):
    """
    Insert the state data into the table.

    Args:
      state_name (str): The name of the state.
      state_data_dict (dict): A dictionary containing the state data the keys:
                            'totală' - area, 'vecini' - neighbors, 'fus orar' - timezone,
                            'densitate' - density, 'estimare' - population, 'limbi oficiale' - lang,
                            'sistem politic' - political_system, 'capitala' - capital.

    Returns:
      None

    Raises:
        Prints an error message for any exception.
    """
    state_data_list = [
        state_name,
        state_data_dict.get('totală', None),
        state_data_dict.get('vecini', None),
        state_data_dict.get('fus orar', None),
        state_data_dict.get('densitate', None),
        state_data_dict.get('estimare', None),
        state_data_dict.get('limbi oficiale', None),
        state_data_dict.get('sistem politic', None),
        state_data_dict.get('capitala', None)
    ]
    try:
        print(f"Inserting for {state_name}")

        insert_query = '''
            INSERT INTO states (name, area, neighbors, timezone, density, population, lang, political_system, capital)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        print("Data inserted successfully")

        cursor.execute(insert_query, state_data_list)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
