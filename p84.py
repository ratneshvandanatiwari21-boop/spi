#read the file
f=None
try:
	filename=input("File name to be open: ")
	f=open(filename,"r")
	contents=f.read()
	print(contents)
except FileNotFoundError:
	print("File does not exists")