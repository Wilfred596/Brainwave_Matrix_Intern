import sqlite3

def init_db():
    conn = sqlite3.connect('Inventory_Data.db')
    cursor = conn.cursor()
    print('Inventory Database has been Created')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserName TEXT PRIMARY KEY AUTOINCREMENT,
            Password TEXT BLOB NOT NULL)''')
    print('Users Table has been Created')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Quantity INTEGER NOT NULL,
            Price REAL NOT NULL)''')
    print('Products Table has been Created')

    conn.commit()
    conn.close()

