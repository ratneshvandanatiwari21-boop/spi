#reverse number
'''
num=123
while num>0:
	r=num%10 #123%10=3,12%10=2,1%10=1
	print(r,end="")#3,2,1
	num=num//10 ##123//10=12,12//10=1,1//10=0
'''
num=135
rev=0
while num>0:
	r=num%10 
	rev=rev*10+r
	num=num//10 
print(rev)