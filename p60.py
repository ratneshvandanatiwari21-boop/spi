#

def search(lt,n):
	le=len(lt)
	for i in range(le):
		if lt[i]==n:
			return(i)
		return (False)
lt=[3,43,45,54,32,98,321]
print(search(lt,45))