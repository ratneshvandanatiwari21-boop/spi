#simple calculator by class

class SimCal:
	def add(self,x,y):
		return(x+y)
	def sub(self,x,y):
		return(x-y)
	def mul(self,x,y):
		return(x*y)
	def div(self,x,y):
		return(x/y)



sc=SimCal()
sum=sc.add(12,30)
sub=sc.sub(30,12)
mul=sc.mul(6,3)
div=sc.div(6,3)
print("SUM is",sum)
print("Substraction is",sub)
print("Multiply is",mul)
print("Division is",div)

