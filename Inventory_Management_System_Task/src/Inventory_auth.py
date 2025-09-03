import sqlite3

def register(UserName, Password):
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users VALUES (?, ?)", (UserName, Password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def login(UserName, Password):
    conn = sqlite3.connect('Inventory_Data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE UserName=? AND Password=?", (UserName, Password))
    result = cursor.fetchone()
    conn.close()
    return result is not None
