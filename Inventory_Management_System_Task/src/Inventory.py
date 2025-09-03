import sqlite3

def add_product(Name, Quantity, Price):
    if Quantity < 0 or Price < 0:
        return "Invalid quantity or price."
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Products (Name, Quantity, Price) VALUES (?, ?, ?)", (Name, Quantity, Price))
    conn.commit()
    conn.close()
    return "Product Added."

def update_product(Product_Id, Quantity, Price):
    if Quantity < 0 or Price < 0:
        return "Invalid Quantity or Price."
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Products SET Quantity=?, Price=? WHERE Id=?", (Quantity, Price, Product_Id))
    conn.commit()
    conn.close()
    return "Product Updated."

def delete_product(Product_Id):
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Products WHERE Id=?", (Product_Id,))
    conn.commit()
    conn.close()
    return "Product Deleted."

def get_all_products():
    conn = sqlite3.connect("Inventory_Data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.commit()
    conn.close()

    # return "Product Details" + "\n" + products

    return products

