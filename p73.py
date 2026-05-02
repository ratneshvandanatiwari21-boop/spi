#unit calculate by class


class MyUnit:
	def test(self,bill):
		unit=int(input("entern the unit"))
		if unit<=150:
			bill=unit*2.40
		elif unit>151 and unit<=300:
			bill=150*2.40+(unit-150)*3.00
		else:
			bill=150*2.40+300*3.00+(unit-300)*3.20
		return(bill)
d=MyUnit()
a=d.test(bill)
print(a)
