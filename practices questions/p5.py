class Employee():
	def __init__(self,empid,empname,salary):
		self.empid=empid
		self.empname=empname
		self.salary=salary
	def display(self):
		print(self.empid,self.empname,self.salary)

emp1=Employee(1001,'XYZ',60000)
emp1.display()

emp2=Employee(1002,'ABC',70000)
emp2.display()

emp3=Employee(1003,'XYZ',65000)
emp3.display()
		