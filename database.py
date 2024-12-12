import sqlite3

# Function to connect to the database and create the table
def initialize_database():
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, address, phone, email, password):
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO user_data (name, address, phone, email, password)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, address, phone, email, password))
    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect("form_data.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user_data')
    data = cursor.fetchall()
    conn.close()
    return data
