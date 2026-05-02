#dynamic list sum
list=[]
print("enter the 5 numbers:")
for i in range(0,5):
	n=int(input())
	list.append(n)
print(list)
sum=0
for i in range(0,5):
	sum=sum+list[i]
print(sum)

