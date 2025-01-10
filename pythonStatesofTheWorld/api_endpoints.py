from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import sql
import ops_database
from ops_database import *
app = Flask(__name__)
@app.route('/top-tari-populatie', methods=['GET'])
def top_by_population():
    """
    Returns the top N states by population
    N is query parameter, or defaults to 10
    """
    try:
        limit = request.args.get('limit', default=10, type=int)

        if limit <= 0:
            return jsonify({"Error": "Limit must be a positive integer"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT name, population 
            FROM states 
            WHERE population IS NOT NULL
            ORDER BY population DESC 
            LIMIT %s
        ''', (limit,))


        states = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify(states)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/top-tari-densitate', methods=['GET'])
def top_by_density():
    """
    Returns the top N states by desnity
    N is query parameter, or defaults to 10
    """
    try:
        limit = request.args.get('limit', default=10, type=int)

        if limit <= 0:
            return jsonify({"Error": "Limit must be a positive integer"}), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            SELECT name, density 
            FROM states 
            WHERE density IS NOT NULL
            ORDER BY density DESC 
            LIMIT %s
        ''', (limit,))

        states = cursor.fetchall()
        cursor.close()
        conn.close()

        return jsonify(states)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tari-UTC+2', methods=['GET'])
def states_gmt_2():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name 
        FROM states 
        WHERE timezone = 'UTC+2'
    ''')
    states = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(states)


@app.route('/tari-limba-engleza', methods=['GET'])
def states_english():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name 
        FROM states 
        WHERE lang IN ('engleza', 'engleză', 'limba engleză')
    ''')
    states = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(states)


@app.route('/tari-regim-politic', methods=['GET'])
def states_by_political_system():
    political_system = request.args.get('regim')

    if not political_system:
        return jsonify({"error": "Missing 'regim' query parameter"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    query = sql.SQL('''
        SELECT name 
        FROM states 
        WHERE political_system = %s
    ''')
    cursor.execute(query, (political_system,))
    states = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(states)

def main():
    print("Starting local endpoints")
    app.run(debug=True)

if __name__ == '__main__':
    main()