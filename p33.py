#wap to fibonacci series


n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n=int(input("enter number:"))
print("fibonacci series:")
print(n1,n2,end=" ")
i=1
while i<=n-2:
	n3=n1+n2
	print(n3,end=" ")
	n1=n2
	n2=n3
	i=i+1

