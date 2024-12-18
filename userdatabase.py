import sqlite3

# Function to initialize the database and create the table
def init_userdatabase():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        ''')
        conn.commit()

# Function to insert a new user into the database
def insert_user(username, password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()

# Function to fetch all users (optional, for testing/debugging)
def get_all_users():
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()
    
def check_user_in_database(username, password):
    # Check if a user exists in the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM users WHERE username = ? AND password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()  # Fetch a single matching row (if any)
    conn.close()

    return result is not None  # Returns True if a match is found, False otherwise
        
