class Account:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        self.add_transaction("Account created", initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        self.add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        self.balance -= amount
        self.add_transaction("Withdrawal", amount)

    def add_transaction(self, transaction_type, amount):
        self.transactions.append(f"{transaction_type}: ${amount:.2f}")

    def get_transaction_history(self):
        return self.transactions if self.transactions else ["No transactions yet."]

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nBalance: ${self.balance:.2f}"


class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")
        self.accounts[account_number] = Account(account_number, name, initial_balance)
        print("Account created successfully.")

    def get_account(self, account_number):
        if account_number not in self.accounts:
            raise ValueError("Account not found.")
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        account.deposit(amount)
        print("Deposit successful.")

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        account.withdraw(amount)
        print("Withdrawal successful.")

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        print(account)

    def transaction_history(self, account_number):
        account = self.get_account(account_number)
        for transaction in account.get_transaction_history():
            print(transaction)


# Console-based Menu
def main():
    atm = ATM()

    while True:
        print("\n--- ATM System Menu ---")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transaction History")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                account_number = input("Enter account number: ")
                name = input("Enter account holder name: ")
                initial_balance = float(input("Enter initial balance (or 0): "))
                atm.create_account(account_number, name, initial_balance)

            elif choice == 2:
                account_number = input("Enter account number: ")
                atm.check_balance(account_number)

            elif choice == 3:
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to deposit: "))
                atm.deposit(account_number, amount)

            elif choice == 4:
                account_number = input("Enter account number: ")
                amount = float(input("Enter amount to withdraw: "))
                atm.withdraw(account_number, amount)

            elif choice == 5:
                account_number = input("Enter account number: ")
                atm.transaction_history(account_number)

            elif choice == 6:
                print("Exiting the ATM system. Thank you!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Run the ATM system
if __name__ == "__main__":
    main()
