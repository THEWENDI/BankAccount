class BankAccount:
    
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Balance: ",self.balance)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        else:
            return 0 
        return self

mr_x = BankAccount()
mr_y = BankAccount()

mr_x.deposit(300).deposit(300).deposit(300).withdraw(100).yield_interest().display_account_info()
mr_y.deposit(200).deposit(400).withdraw(700).withdraw(200).withdraw(200).withdraw(100).yield_interest().display_account_info()

