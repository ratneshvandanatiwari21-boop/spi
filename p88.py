#multiple Inheritance

class A:
	def M1(self):
		print("Main M1 huin aur Main class A ka huin...")
class B():
	def M2(self):
		print("Main M2 huin aur Main class B ka huin...")
class C(A,B):
	def M3(self):
		print("Main M3 huin aur Main class C ka huin...")
a=C()
a.M3()
a.M2()
a.M1()