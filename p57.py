import tempconv
print("Enter 1 for c to f")
print("Enter any 2 for f to c")
a=int(input())
if a==1:
	c=float(input("enter temprature"))
	f=tempconv.ctof(c)
	print("temprature in fehrenhite",f)
elif a==2:
	f=float(input("Enter temperature in f :"))
	c=tempconv.ftoc(f)
	print("temprature in degree celecius",c)
else:
	print("error found")
