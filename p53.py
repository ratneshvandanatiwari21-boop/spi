#funtion to count even and odd numbers of list
def count_even_odd(list):
	total_even=0
	total_odd=0
	for i in list:
		if i%2==0:
			total_even+=1	
		else:
			total_odd+=1
	return(total_even,total_odd)
print(count_even_odd([2,3,4,5,6]))
	
	
	