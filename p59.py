#wap prime number from taking input from user.


s=int(input("enter starting:"))
e=int(input("enter ending:"))
for i in range(s,e+1):
	f=0
	for j in range(1, i+1):
		if i%j==0:
			f+=1
	if f==2:
		print(i,"is prime")