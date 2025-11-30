class BankAccount:
    def __init__(self, initial_balance):
        initial_balance = 0
        self.account_balance = float(initial_balance)
    
    def deposit(self, amount):
        amount = float(amount)
        if amount < 0:
            raise ValueError(f"Deposit amount must be more than zero")    
        self.account_balance += amount
        return self.account_balance    
    
    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError(f"Deposit amount must be more than zero")
        
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")

    def get_balance(self):
        return self.account_balance