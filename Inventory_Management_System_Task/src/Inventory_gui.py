import tkinter as tk
from tkinter import messagebox
from Inventory_auth import login, register
from Inventory import add_product, update_product, delete_product, get_all_products
from Inventory_reports import low_stock_alert, sales_summary

class InventoryAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System Login Screen")
        self.UserName = None
        self.login_screen()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear()
        tk.Label(self.root, text="UserName:").pack()
        user_entry = tk.Entry(self.root)
        user_entry.pack()
        tk.Label(self.root, text="Password:").pack()
        pass_entry = tk.Entry(self.root, show="*")
        pass_entry.pack()

        def handle_login():
            if login(user_entry.get(), pass_entry.get()):
                self.UserName = user_entry.get()
                self.dashboard()
            else:
                messagebox.showerror("Error", "Invalid Credentials")

        def handle_register():
            UserName = user_entry.get().strip()
            Password = pass_entry.get().strip()

            # ✅ New validation logic
            if not UserName and not Password:
                messagebox.showerror("Error", "Please Register")
                return

            if register(UserName, Password):
                messagebox.showinfo("Success", "User Account Created.")
            else:
                messagebox.showerror("Error", "UserName exists.")

        tk.Button(self.root, text="Login", command=handle_login).pack()
        tk.Button(self.root, text="Register", command=handle_register).pack()

    def register_screen(self):
        self.clear()
        tk.Label(self.root, text="Create a New User Account").pack()

        tk.Label(self.root, text="UserName").pack()
        new_user = tk.Entry(self.root)
        new_user.pack()

        tk.Label(self.root, text="Password").pack()
        new_pass = tk.Entry(self.root, show="*")
        new_pass.pack()

        def handle_register():
            UserName = new_user.get().strip()
            Password = new_pass.get().strip()

            # Validation checks

            # ✅ New validation logic
            if not UserName and not Password:
                messagebox.showerror("Error", "Please Register before Creating a new User Account.")
                return
            if not UserName or not Password:
                messagebox.showerror("Error", "UserName and Password cannot be empty.")
                return
            if " " in UserName:
                messagebox.showerror("Error", "UserName cannot contain spaces.")
                return
            if len(Password) < 4:
                messagebox.showerror("Error", "Password must be at least 4 characters.")
                return

            if register(UserName, Password):
                messagebox.showinfo("Success", "User Account Created successfully.")
                self.login_screen()
            else:
                messagebox.showerror("Error", "Username already exists.")

        tk.Button(self.root, text="Submit", command=handle_register).pack()
        tk.Button(self.root, text="Back", command=self.login_screen).pack()

    def dashboard(self):
        self.clear()
        tk.Label(self.root, text=f"Welcome, {self.UserName}").pack()
        tk.Button(self.root, text="Add Product", command=self.add_product_ui).pack()
        tk.Button(self.root, text="View Inventory", command=self.view_inventory).pack()
        tk.Button(self.root, text="Low Stock Alert", command=self.show_alerts).pack()
        tk.Button(self.root, text="Sales Summary", command=self.show_summary).pack()
        tk.Button(self.root, text="Logout", command=self.login_screen).pack()

    def add_product_ui(self):
        self.clear()
        tk.Label(self.root, text="Product Name").pack()
        name = tk.Entry(self.root)
        name.pack()
        tk.Label(self.root, text="Quantity").pack()
        qty = tk.Entry(self.root)
        qty.pack()
        tk.Label(self.root, text="Price").pack()
        price = tk.Entry(self.root)
        price.pack()

        def submit():
            try:
                msg = add_product(name.get(), int(qty.get()), float(price.get()))
                messagebox.showinfo("Info", msg)
                self.dashboard()
            except:
                messagebox.showerror("Error", "Invalid input")

        tk.Button(self.root, text="Submit", command=submit).pack()
        tk.Button(self.root, text="Back", command=self.dashboard).pack()

    def view_inventory(self):
        self.clear()
        products = get_all_products()
        for p in products:
            tk.Label(self.root, text=f"ID:{p[0]} | {p[1]} | Qty:{p[2]} | ₹{p[3]}").pack()
        tk.Button(self.root, text="Back", command=self.dashboard).pack()

    def show_alerts(self):
        alerts = low_stock_alert()
        if alerts:
            msg = "\n".join([f"{a[1]} - Qty:{a[2]}" for a in alerts])
        else:
            msg = "No low stock items."
        messagebox.showinfo("Low Stock", msg)

    def show_summary(self):
        total = sales_summary()
        messagebox.showinfo("Sales Summary", f"Total Inventory Value: ₹{total:.2f}")
