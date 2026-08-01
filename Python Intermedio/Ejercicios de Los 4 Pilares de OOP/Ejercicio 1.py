class BankAccount:
    balance = 500

    def add_funds(self, amount):
        self.balance += amount

    def remove_funds(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance

    def remove_funds(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError("Withdrawal would bring the balance below the minimum balance.")
        self.balance -= amount

def main():
    account = BankAccount()
    account.add_funds(100)
    account.remove_funds(200)
    print(account.balance)

    savings_account = SavingsAccount(min_balance=100)
    savings_account.add_funds(100)
    savings_account.remove_funds(200)
    print(savings_account.balance)

    try:
        savings_account.remove_funds(400)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
