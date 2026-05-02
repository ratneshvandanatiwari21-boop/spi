lst=[]

for i in range(5):
	n=int(input('Enter the Numbers :'))
	lst.append(n)
lst.sort()
print('Ascending Order List',lst)
lst.reverse()
print('Decending Order List',lst)    
