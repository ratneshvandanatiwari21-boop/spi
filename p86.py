#Inherritence

class BullDog():
	def Grawl(self):
		print("Bruno....")
		print("Gur... Gur...")
class PetDog(BullDog):
	def Bark(self):
		print("Sheru....")
		print("Bho... Bho...")
d=PetDog()
d.Bark()
d.Grawl()