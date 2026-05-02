class Bank:
	def __init__(self,acno,name,balance):
		self.acno=acno
		self.name=name
		self.balance=balance
	def deposite(self):
		amount = float(input("Enter amount to be Deposited: "))
       	 	self.balance += amount
        	print("Amount Deposited:", amount)
x=int(input("Account No:"))
y=input("Name: ")
z=int(input("Balance"))
b=Bank(x,y,z)
dep=d.deposite()
print("Total amount: ",dep)

		