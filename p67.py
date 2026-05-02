#pattern A printing

h=5
w=5
for i in range(1,h+1):
	for j in range(1,w+1):
		if i==1 and j==3 or i==2 and j==2 or i==2 and j==4 or i==3 or i==1 and j==4 or i==5 and j==4 or i==1 and j==5 or i==5 and j==5:
			print("*",end=" ")
		else:
			print(" ",end=" ")
	print()