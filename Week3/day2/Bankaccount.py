<<<<<<< HEAD
class BankAccount:
    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.accountname = accountname
        return None
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self

    # def user_createAccount(self,int_rate, balance):
    #     self.account = BankAccount(int_rate, balance) #pass in accountname when creating account, then append to list - can use to loop through accounts in classmethod below.
    #     User.user_accounts.append(self) #getting error here - why? Same as BankAccount?
    
    def display_users_account_info(self):
        # print(self.account.balance)
        self.account.display_account_info()
        return self




user1 = BankAccount(0.02, 200,)

user2 = BankAccount(0.01,100,)
user1.display_account_info()

Bob = User('Bob',"gmail.com")

Bob.make_deposit(80)
Bob.display_users_account_info()
=======
class BankAccount:
    def __init__(self,int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        # self.accountname = accountname
        return None
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02,balance=0)

    def make_deposit(self,amount):
        self.account.deposit(amount)

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
        return self

    # def user_createAccount(self,int_rate, balance):
    #     self.account = BankAccount(int_rate, balance) #pass in accountname when creating account, then append to list - can use to loop through accounts in classmethod below.
    #     User.user_accounts.append(self) #getting error here - why? Same as BankAccount?
    
    def display_users_account_info(self):
        # print(self.account.balance)
        self.account.display_account_info()
        return self




user1 = BankAccount(0.02, 200,)

user2 = BankAccount(0.01,100,)
user1.display_account_info()

Bob = User('Bob',"gmail.com")

Bob.make_deposit(80).display_users_account_info()
>>>>>>> 8a4770cb25b054a607ca935dd43ab4814dc86942
