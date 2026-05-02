#EH
#simple calculator
try:
	a=int(input("Enter the first number: "))
	b=int(input("Enter the second number: "))
	c=a/b
	print(c)
except ValueError:
	print("Only Integers value are allowd")
except ZeroDivisionError:
	print("Answer is infinite")
finally:
	print("Thanks for your calculation.....")