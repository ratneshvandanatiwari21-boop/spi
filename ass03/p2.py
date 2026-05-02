"""Write a program in python to take a string as input. Now check given string is palindrome or not."""


a=input("Enter String: ")
str=a.lower()
b="".join(reversed(str))
print(b)
if str==b:
	print("String is Palindrome")
else:
	print("String is not Palindrome")