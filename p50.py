#function to check even or odd
def fun1(a):
	if a%2==0:
		return"even"
	else:
		return"odd"
a=int(input("enter the number:"))
print(fun1(a))
