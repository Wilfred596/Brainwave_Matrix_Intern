import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
class ATMGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("🏦 ATM Interface Screen")
        self.pin = "1234"
        self.balance = 1000.0

        self.create_login_screen()

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def create_login_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="🔐 Enter PIN:", font=("Arial", 14)).pack(pady=10)
        self.pin_entry = tk.Entry(self.master, show="*", font=("Arial", 14))
        self.pin_entry.pack(pady=5)
        tk.Button(self.master, text="Login", command=self.authenticate, font=("Arial", 12)).pack(pady=10)

    def authenticate(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "❌ Incorrect PIN")

    def create_main_menu(self):
        self.clear_screen()
        tk.Label(self.master, text="📋 ATM Menu", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Button(self.master, text="Check Balance", command=self.check_balance, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.master, text="Deposit", command=self.deposit_screen, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.master, text="Withdraw", command=self.withdraw_screen, font=("Arial", 12)).pack(pady=5)
        tk.Button(self.master, text="Exit", command=self.master.quit, font=("Arial", 12)).pack(pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", f"💰 Current Balance: ₹{self.balance:.2f}")

    def deposit_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="💵 Enter amount to deposit:", font=("Arial", 14)).pack(pady=10)
        self.amount_entry = tk.Entry(self.master, font=("Arial", 14))
        self.amount_entry.pack(pady=5)
        tk.Button(self.master, text="Deposit", command=self.deposit, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Arial", 12)).pack()

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Success", f"✅ ₹{amount:.2f} deposited.")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "❌ Invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "❌ Please enter a valid number.")

    def withdraw_screen(self):
        self.clear_screen()
        tk.Label(self.master, text="💸 Enter amount to withdraw:", font=("Arial", 14)).pack(pady=10)
        self.amount_entry = tk.Entry(self.master, font=("Arial", 14))
        self.amount_entry.pack(pady=5)
        tk.Button(self.master, text="Withdraw", command=self.withdraw, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.master, text="Back", command=self.create_main_menu, font=("Arial", 12)).pack()

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if 0 < amount <= self.balance:
                self.balance -= amount
                messagebox.showinfo("Success", f"✅ ₹{amount:.2f} withdrawn.")
                self.create_main_menu()
            else:
                messagebox.showerror("Error", "❌ Insufficient balance or invalid amount.")
        except ValueError:
            messagebox.showerror("Error", "❌ Please enter a valid number.")

# 🧪 Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    app = ATMGUI(root)
    root.mainloop()

