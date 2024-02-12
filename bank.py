class CashMachine:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"Withdrawn {amount}. New balance: {self.balance}"

    def print_statement(self):
        return f"Current balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def return_card(self):
        return "Card returned. Thank you!"

# Example usage
cash_machine = CashMachine()

while True:
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Print statement")
    print("4. Deposit money")
    print("5. Return card")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("Current balance:", cash_machine.check_balance())
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        print(cash_machine.withdraw(amount))
    elif choice == '3':
        print(cash_machine.print_statement())
    elif choice == '4':
        amount = float(input("Enter amount to deposit: "))
        print(cash_machine.deposit(amount))
    elif choice == '5':
        print(cash_machine.return_card())
        break
    else:
        print("Invalid choice. Please try again.")
