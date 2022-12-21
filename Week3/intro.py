<<<<<<< HEAD
class BankAccount:
    #declaring class attribute, has to be outside init
    all_accounts = []

    def __init__(self, int_rate, balance, accountname): 
        self.int_rate = int_rate
        self.balance = balance
        self.accountname = accountname
        #need to add to all_account list for class function
        BankAccount.all_accounts.append(self)

class User:
    
    user_accounts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def user_createAccount(self,int_rate, balance, accountname):
        self.account = BankAccount(int_rate, balance, accountname) #pass in accountname when creating account, then append to list - can use to loop through accounts in classmethod below.
        User.user_accounts.append(self) #getting error here - why? Same as BankAccount?

Bob = User('Bob',"gmail.com")

Bob.user_createAccount(0.01,90,'capitol1')

=======
class BankAccount:
    #declaring class attribute, has to be outside init
    all_accounts = []

    def __init__(self, int_rate, balance, accountname): 
        self.int_rate = int_rate
        self.balance = balance
        self.accountname = accountname
        #need to add to all_account list for class function
        BankAccount.all_accounts.append(self)

class User:
    
    user_accounts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def user_createAccount(self,int_rate, balance, accountname):
        self.account = BankAccount(int_rate, balance, accountname) #pass in accountname when creating account, then append to list - can use to loop through accounts in classmethod below.
        User.user_accounts.append(self) #getting error here - why? Same as BankAccount?

Bob = User('Bob',"gmail.com")

Bob.user_createAccount(0.01,90,'capitol1')

>>>>>>> 8a4770cb25b054a607ca935dd43ab4814dc86942
Bob.user_createAccount(0.01, 0, "Fishing").user_display_info()