def fun1(n):
	if n==0 or n==1:
		return(1)
	else:
		return(n*fun1(n-1))
x=int(input("enter the number"))
f=fun1(x)
print("the factorial of", x ,"is:", f)
