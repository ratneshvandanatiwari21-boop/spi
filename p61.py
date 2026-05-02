def chalu(n,i=1):
	if(i<=n):
		print(fibo(i-1),end=" ")
		chalu(n,i+1)
	else:
		return(0)
def fibo(n):
	if n==0 or n==1:
		return(n)
	else:
		return(fibo(n-1)+fibo(n-2))
n=int(input("Enter the no. of terms:"))
chalu(n)
