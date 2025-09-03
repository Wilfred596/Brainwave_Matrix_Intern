from Inventory_db import init_db
import tkinter as tk
from Inventory_gui import InventoryAppGUI

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    root.geometry("400x400")
    app = InventoryAppGUI(root)
    root.mainloop()
