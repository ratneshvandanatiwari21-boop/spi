#Armstrong or not
n=int(input('Enter the Number: '))
tem=n
sum=0
while tem>0:
	r=tem%10
	sum=sum+r**3
	tem=tem//10
if sum==n:
	print("Armstrong")
else:
	print("Not Armstrong")
