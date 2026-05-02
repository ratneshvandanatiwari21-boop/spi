from django.shortcuts import render, redirect
from . models import Employee
# Create your views here.
def index(req):
    emp=Employee.objects.all() # Select * from employee
    return render(req,"index.html",{"emp" : emp})
def empreg(req):
    if req.method=='POST':
        empid=req.POST['empid']
        empname=req.POST['empname']
        department=req.POST['department']
        salary=req.POST['salary']
        #ORM (Object Relationship Mapping)
        emp=Employee(empid=empid, empname=empname, department=department, salary=salary)
        emp.save()
        return redirect('index')
    return render(req, "empreg.html")
def deleteemp(req, empid):
    emp=Employee.objects.get(empid=empid) # select * from Employee where empid=empid
    emp.delete()
    return redirect('index')

def editemp(req, empid):
    emp=Employee.objects.get(empid=empid) # select * from Employee where empid=empid
    return render(req, "editemp.html", {"emp": emp})

def updateemp(req):
    empid=req.POST['empid']
    empname=req.POST['empname']
    department=req.POST['department']
    salary=req.POST['salary']
    Employee.objects.filter(empid=empid).update( empname=empname, department=department, salary=salary)
    return redirect('index')