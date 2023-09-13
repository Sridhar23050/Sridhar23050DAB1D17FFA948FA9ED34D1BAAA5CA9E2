
class BankAccount:
    def __init__(self, acc_num, acc_holder_name, acc_balance):
        self.__acc_num = acc_num
        self.__acc_holder_name = acc_holder_name
        self.__acc_balance = acc_balance

    def deposit(self, amount):
        self.__acc_balance += amount

    def withdraw(self, amount):
        if amount > self.__acc_balance:
            print("Insufficient balance")
        else:
            self.__acc_balance -= amount

    def display_balance(self):
        print("Account balance:", self.__acc_balance)

# Creating an instance of BankAccount class
my_account = BankAccount("123456789", "John Doe", 5000)

# Testing deposit functionality
my_account.deposit(1000)
my_account.display_balance()

# Testing withdrawal functionality
my_account.withdraw(2000)
my_account.display_balance()
