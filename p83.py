#devolop a program in python in file

f=open("emp.pdf","a")
empid=int(input("Enter ID: "))
empname=input("Enter Name: ")
empsalary=int(input("Enter Salary: "))

f.write("Employee ID: "+str(empid)+"\n"+"Employee Name: "+empname+"\n"+"Employee Salary: "+str(empsalary)+"\n")

f.close()
print("Information saved")