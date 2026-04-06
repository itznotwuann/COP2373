# BankAcct class definition
class BankAcct:

    # Constructor to initialize account information
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate  # annual interest rate (e.g., 0.05 for 5%)

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.amount -= amount

    # Method to adjust the interest rate
    def set_interest_rate(self, new_rate):
        if new_rate >= 0:
            self.interest_rate = new_rate
        else:
            print("Interest rate must be non-negative.")

    # Method to return the current balance
    def get_balance(self):
        return self.amount

    # Method to calculate interest based on number of days
    def calculate_interest(self, days):
        # Simple interest formula: A = P * r * t
        # t is time in years → days / 365
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    # String representation of the account
    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate:.2%}")


# Test function to demonstrate all methods
def test_bank_account():
    # Create a bank account object
    acct = BankAcct("Alice Smith", "123456", 1000.0, 0.05)

    # Display initial account info
    print("Initial Account:")
    print(acct)
    print()

    # Test deposit
    acct.deposit(500)
    print("After Deposit of $500:")
    print(f"Balance: ${acct.get_balance():.2f}")
    print()

    # Test withdrawal
    acct.withdraw(200)
    print("After Withdrawal of $200:")
    print(f"Balance: ${acct.get_balance():.2f}")
    print()

    # Test interest rate adjustment
    acct.set_interest_rate(0.04)
    print("After Changing Interest Rate to 4%:")
    print(acct)
    print()

    # Test interest calculation
    days = 30
    interest = acct.calculate_interest(days)
    print(f"Interest for {days} days: ${interest:.2f}")
    print()


# Run test function if file is executed
if __name__ == "__main__":
    test_bank_account()