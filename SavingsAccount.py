from Account import Account
class Savings(Account):
    def __init__(self, owner, balance=0, withdrawal_limit = 100):
        super().__init__(owner, balance)
        self.interest_rate = 0.02  #Example interest rate
        self.withdrawal_limit = withdrawal_limit

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f" Interest of {interest} applied. New balance: ${self.get_balance()}")

    def withdraw(self,amount):
        if amount>self.withdrawal_limit:
            print(f"Withdrawal amount exceeds the limit of ${self.withdrawal_limit}.")
        else:
            super().withdraw(amount)


#Test Savings Account
print("---Savings Account---")
savings = Savings("Alice", 1000)
print(f"Initial Balance: {savings.get_balance()}")
savings.deposit(500)
savings.withdraw(200)
savings.apply_interest() #should be successful

