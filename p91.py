#hybrid inheritance

class A:
	def M1(self):
		print("Main M1 huin aur Main class A ka huin...")
class B(A):
	def M2(self):
		print("Main M2 huin aur Main class B ka huin...")
class C(A):
	def M3(self):
		print("Main M3 huin aur Main class C ka huin...")
class D(B,C):
	def M4(self):
		print("Main M4 huin aur Main class D ka huin...")
w=D()
w.M4()
w.M3()
w.M2()
w.M1()