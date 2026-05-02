
class Base:
	def showBase(self):
		print("This massage from base class")
class Derived(Base):
	def showDerived(self):
		print("This massage from drived class")
d=Derived()
d.showDerived()
d.showBase()