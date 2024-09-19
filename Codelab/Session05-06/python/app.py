import sqlite3
import re

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello LG CNS'


def get_db_connection():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        # Handle connection errors and return a JSON error response
        return jsonify({"error": "Database connection failed", "details": str(e)}), 500


# Input validation function
def is_valid_query(query):
    # Simple validation to ensure query contains only letters, numbers, and spaces
    # You can add more validation rules if needed
    return bool(re.match("^[a-zA-Z0-9]*$", query)) and len(query) > 0 and len(query) <= 100


# Search function with secure SQL query
@app.route('/products/search')
def search_products():
    query = request.args.get('query')

    # Validate the query
    if not query or not is_valid_query(query):
        return jsonify({"error": "Invalid search query"}), 400

    # Parameterized query to prevent SQL injection
    sql = "SELECT * FROM products WHERE name LIKE ?"

    try:
        conn = get_db_connection()
        if isinstance(conn, tuple):  # Handle connection failure
            return conn  # Already a JSON response

        # Use parameterized query with wildcard search
        results = conn.execute(sql, ('%' + query + '%',)).fetchall()
        conn.close()

        # Convert results to a list of dictionaries
        product_list = [dict(row) for row in results]
        return jsonify(product_list), 200
    except sqlite3.Error as e:
        # Handle any database errors
        return jsonify({"error": "Database error", "details": str(e)}), 500
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run()
