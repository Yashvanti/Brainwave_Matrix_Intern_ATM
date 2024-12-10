import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.balance = 0.0

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Welcome to the ATM", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        # Balance Label
        self.balance_label = tk.Label(self.root, text=f"Current Balance: ${self.balance:.2f}", font=("Helvetica", 14))
        self.balance_label.pack(pady=10)

        # Deposit Button
        self.deposit_button = tk.Button(self.root, text="Deposit Money", command=self.deposit, width=20)
        self.deposit_button.pack(pady=5)

        # Withdraw Button
        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", command=self.withdraw, width=20)
        self.withdraw_button.pack(pady=5)

        # Check Balance Button
        self.check_balance_button = tk.Button(self.root, text="Check Balance", command=self.check_balance, width=20)
        self.check_balance_button.pack(pady=5)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, width=20)
        self.exit_button.pack(pady=5)

    def deposit(self):
        amount = self.get_amount("Deposit")
        if amount is not None:
            self.balance += amount
            self.update_balance()

    def withdraw(self):
        amount = self.get_amount("Withdraw")
        if amount is not None:
            if amount <= self.balance:
                self.balance -= amount
                self.update_balance()
            else:
                messagebox.showerror("Error", "Insufficient funds.")

    def check_balance(self):
        messagebox.showinfo("Balance", f"Your current balance is: ${self.balance:.2f}")

    def get_amount(self, action):
        amount_str = tk.simpledialog.askstring("Input", f"Enter amount to {action.lower()}:")
        if amount_str is not None:
            try:
                amount = float(amount_str)
                if amount > 0:
                    return amount
                else:
                    messagebox.showerror("Error", "Please enter a positive number.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please enter a number.")
        return None

    def update_balance(self):
        self.balance_label.config(text=f"Current Balance: ${self.balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.geometry("300x300")
    root.mainloop()