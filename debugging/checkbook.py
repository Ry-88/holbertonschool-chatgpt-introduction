#!/usr/bin/python3
"""
checkbook.py

A simple command-line checkbook application that allows users to deposit,
withdraw, and check their account balance.

Usage:
    Run the program and interact through prompts:
    > What would you like to do? (deposit, withdraw, balance, exit):
"""

class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance tracking.
    """
    def __init__(self):
        """
        Initializes the checkbook with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a positive amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit. Must be greater than 0.
        """
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a positive amount from the checkbook if funds are sufficient.

        Parameters:
            amount (float): The amount to withdraw. Must be <= current balance.
        """
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop for user interaction.
    Allows user to choose actions and handles input errors gracefully.
    """
    cb = Checkbook()
    while True:
        action = input("\nWhat would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            print("Thank you for using the Checkbook. Goodbye!")
            break
        elif action in ['deposit', 'withdraw']:
            try:
                amount_str = input("Enter the amount: $").strip()
                amount = float(amount_str)
                if action == 'deposit':
                    cb.deposit(amount)
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again (deposit, withdraw, balance, exit).")

if __name__ == "__main__":
    main()
