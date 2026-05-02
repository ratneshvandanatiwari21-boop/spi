# non static class

class Student:
	def __init__(self,strollno,stname,stfee):
		self.strollno=strollno
		self.stname=stname
		self.stfee=stfee
	def getvalue(self):
		print("Roll No: ",self.strollno)
		print("NAME: ",self.stname)
		print("FEE: ",self.stfee)

a=int(input("Enter roll no:"))
b=input("Enter name:")
c=int(input("Enter Fee:"))
d=Student(a,b,c)
d.getvalue()



