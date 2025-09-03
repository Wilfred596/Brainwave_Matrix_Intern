import sqlite3

def low_stock_alert(threshold=5):
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE Quantity < ?", (threshold,))
    alerts = cursor.fetchall()
    conn.commit()
    conn.close()
    return alerts

def sales_summary():
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(Quantity * Price) FROM Products")
    total = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return total if total else 0
