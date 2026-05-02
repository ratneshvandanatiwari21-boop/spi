#area and perimeter by class

class Rectangle:
	def area(self,l,b):
		return(l*b)
	def per(self,l,b):
		return(2*(l+b))
d=Rectangle()
n=int(input("enter the length"))
m=int(input("enter the breadth"))
area=d.area(n,m)
per=d.per(n,m)
print(area)
print(per)


