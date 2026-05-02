#multi Level

class A:
	def M1(self):
		print("I am B.tech student")
class B(A):
	def M2(self):
		print("I am from Ayodhya")
class C(B):
	def M3(self):
		print("Myself Ratnesh Tiwari...")
a=C()
a.M3()
a.M2()
a.M1()