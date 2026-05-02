#exception handling

def fun(x,y):
	try:
		result=(x/y)
	except ZeroDivisionError:
		print("infinite....")
	else:
		print(result)
try:
	a=int(input("Enter the first number: "))
	b=int(input("Enter the second number: "))
	fun(a,b)
except ValueError:
	print("only use integers")
finally:
	print("Visit again")
		