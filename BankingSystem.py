#PROJECT
#Write a python program to replicate a Banking system. The following features are mandatory:
        #1.Account login
        #2. Amount Depositing
        #3. Amount Withdrawal

class Banking_System:
    def __init__(self,holder,ano,uname,pword,bal=0):
        self.account_holder=holder
        self.account_no=ano
        self.username=uname
        self.password=pword
        self.balance=bal

    def login(self):
        a_no=int(input("Enter account number: "))
        uname=input("enter username: ")
        pword=input("Enter password: ")
        if a_no==self.account_no and uname==self.username and pword==self.password:
            print(f"Hi {self.account_holder} welcome to BDI Banking System")
            while True:
                print("Press 1 for deposit ")
                print("Press 2 for withdraw")
                print("Press 3 for check balance")
                print("Press 4 to logout")
                choice=int(input("Enter your choice: "))
                if choice==1:
                    account1.deposit()
                elif choice==2:
                    account1.withdraw()
                elif choice==3:
                    account1.checkbalance()
                elif choice==4:
                    print("You are going to logout ")
                    break
                else:
                    break
        else:
            print("Please enter valid username or password")

    def deposit(self):
        amount=int(input("Enter the amount to be deposit: "))
        self.balance+=amount
        print(f"An amount of rupees {amount} has credited to your account")
        print(f"your new balance is {self.balance}")
    def withdraw(self):
        wamount=int(input("Enter the amount to be withdraw: "))
        if self.balance>=wamount:
            self.balance-=wamount
            print(f"An amount of rupees {wamount} has debited from your account")
            print(f"your new balance is {self.balance}")
        else:
            print("Insufficient balance")
    def checkbalance(self):
        print(f"your balance is {self.balance}")

account1=Banking_System("zehrin",3434,"anha123","p8899")
account1.login()