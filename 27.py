list=[]
print("enter the 3 numbers")
for i in range(0,3):
	n=int(input())
	list.append(n)
print(list)
n=int(input("enter the searching number:"))
c=0
for i in range(0,3):
	if n==list[i]:
		c=c+1
if c==1:
	print("yes")
else:
	print("No")