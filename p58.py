#function
a=eval(input("enter the first number:"))
b=eval(input("enter the second number:"))
def calc(x,y):
	sum=x+y
	sub=x-y
	mult=x*y
	div=x/y
	return([sum,sub,mult,div])
c=calc(a,b)
print(c)
