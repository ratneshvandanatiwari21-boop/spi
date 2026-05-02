try:
	a=int(input('Enter the First Number:'))
	b=int(input('Enter the second Number:'))
	n=a/b
	print(n)
except ZeroDivisionError:
	print('Zero Division Error')