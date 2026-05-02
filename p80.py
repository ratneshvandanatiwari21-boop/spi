#EH
#simple calculator
try:
	a=int(input("Enter the first number: "))
	b=int(input("Enter the second number: "))
	c=a+b
	print(c)
except ValueError:
	print("Alphabets are not allowed")
