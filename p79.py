class Bank:
    def __init__(self,acno,name,balance):
        self.acno=acno
        self.name=name
        self.balance=balance   
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("New Balance=",self.balance)

    def withdraw(self,amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            print(amount,"amount withdraw,New Balance:",self.balance)
        else:
            print("Insufficient Balance")    

    def enquiry(self):
        print("Your current balance =",self.balance)        

acno=int(input("Enter your acccount number:"))
name=input("Enter your name:")
balance=int(input("Enter balance:"))

b=Bank(acno,name,balance)

b.enquiry()
amount=int(input("Enter amount to deposit:"))
b.deposit(amount)
amount=int(input("Enter amount to withdraw:"))
b.withdraw(amount)