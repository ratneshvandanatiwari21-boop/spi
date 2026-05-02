import cmath 
a=int(input("enter coeffient of x^2:"))
b=int(input("enter coeffient of x:"))
c=int(input("enter constant:"))

d=b**2-4*a*c
if d<0:
	print("roots are imaginary")
else:
	root1=(-b+cmath.sqrt(b*b-4*a*c))/(2*a)
	root2=(-b-cmath.sqrt(b*b-4*a*c))/(2*a)
	print(root1,root2)