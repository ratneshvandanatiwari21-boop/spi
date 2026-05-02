#function to sum all element of a list
def sum_list(list):
	total=0
	for i in list:
		total=total+i
	return(total)
list=[]

print(sum_list(list))