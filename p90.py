class Shape:
	def setValue(self,a):
		return(a)		
class Square(Shape):	
	def sArea(self,a):
		return(a*a)
class Cube(Shape):
	def cVolume(self,a):
		return(a*a*a)
x=int(input("Enter the side: "))
c=Cube()
s=Square()
d=c.cVolume(x)
e=s.sArea(x)
f=c.setValue(x)
print("Side is: ",f)
print("Area is: ",e)
print("Volume is: ",d)
