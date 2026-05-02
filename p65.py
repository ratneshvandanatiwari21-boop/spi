#pattern printing

n=5
p=1
for i in range(1,n+1):
	for j in range(i):
		print(p,end="  ")
		p=p+1
	print()