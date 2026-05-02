#if statement
"""n=int(input("enter a number"))
if n==1:
	print("Hlw Ratnesh....")
print("Hlw ratnesh")"""


#greater number
"""n=int(input("enter a 1st number"))
m=int(input("enter a 2nd number"))
if n>m:
	print("1st number is greater then 2nd number")
else:
	print("1st number is smaller then 2nd number")"""


#WAP to find roots of quadratic equation
'''import math as mt
a=eval(input("enter cofficient of x^2:"))
b=eval(input("enter cofficient of x:"))
c=eval(input("enter number c:"))
d=b*b-4*a*c
if d<0:
	print("roots are real")
else:
	r1=(+b+mt.sqrt(d))/(2*a)
	r2=(-b+mt.sqrt(d))/(2*a)
	print("Root1=",r1)
	print("Root2=",r2)'''


#wap to find electrcity bills
'''unit=eval(input("enter the UNIT:"))
if unit<=150:
	print("Bill is Rs:",unit*2.40)
elif unit>150 and unit<=300:
	print("Bill is Rs:",150*2.40+(unit-150)*3.00)
else:
	print("Bill is Rs:",150*2.40+150*3.00+(unit-300)*3.20)'''

#WAP temeprature measurment

'''print("Enter 1 for c to f")
print("Enter 2 for f to c")
a=int(input())
if a==1:
	c=float(input("enter temprature"))
	f=(9*c)/5+32
	print(f)
elif a==2:
	f=float(input("Enter temperature in f :"))
	c=(f-32)*5/9
	print(c,"c")
else:
	print("input is invalied")'''

#wap to fibonacci series
'''n=int(input("enter number:"))
n1=0
n2=1
print("fibonacci series:")
print(n1,n2,end=" ")
i=1
while i<=n-2:
	n3=n1+n2
	print(n3,end=" ")
	n1=n2
	n2=n3
	i=i+1'''

#wap to factorial
'''n=int(input("enter number:"))
f=1
i=1
if n<0:
	print("not found:")
elif n==0:
	print("factorial is:1")
else:
	while i<=n:
		f=f*i
		i=i+1
	print(f)'''
#total salary
bs=int(input("basic salary"))
if bs<=4000:
	h=bs*(10/100)
	d=bs*(50/100)
	gs=bs+h+d
	print("gs is",gs)
elif bs>4001 and bs<=8000:
	h=bs*(15/100)
	d=bs*(60/100)
	gs=bs+h+d
	print("gs is",gs)
elif bs>8001 and bs<=12000:
	h=bs*(20/100)
	d=bs*(70/100)
	gs=bs+h+d
	print("gs is",gs)
else:
	h=bs*(25/100)
	d=bs*(80/100)
	gs=bs+h+d
	print("gs is",gs)

	
		
	
	








