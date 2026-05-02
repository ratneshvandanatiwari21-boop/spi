#WAP to disply year week and days

a=int(input("enter the days:"))
b=a//365
c=(a%365)//7
d=(a%365)%7
print(b,"Year",c,"Week",d,"Day")

