#volume of cubiod

class Cubiod:
	def __init__(self,l,b,h):
		self.l=l
		self.b=b
		self.h=h
	def cubd(self):
		return(self.l*self.b*self.h)
x=int(input("Length: "))
y=int(input("Breadth: "))
z=int(input("Height: "))
c=Cubiod(x,y,z)
volume=c.cubd()
print("Volume is: ",volume,"m^3")