from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import NameForm
from .models import Applicants


def home(request):
    # stud=Employee.objects.get(pk=101)
    # val=request.GET['num1']
    return render(request, 'Home.html')

def add1(request):
    global val
    val=request.POST.get('num2')
    print("val=",val)
    stu = Applicants.objects.get(pk=val)
    return render(request,'show.html',{'result': stu})
   
def UPDATE(request):
    # valu=request.POST.get('num2')
    print("value=",val)
    cand = Applicants.objects.get(pk=val)
    print("employee=",cand)
    

    if request.method == 'POST':
        # form = EmployeeForm(request.POST, instance=employee)
        BIb=request.POST.get('BiB')
        print("prod.BIb=",BIb)
        chip1=request.POST.get('Chipcode1')
        print("prod.chipcode1=",chip1)
        chip2=request.POST.get('Chipcode2')
        print("prod.chipcode1=",chip2)
        Y=Applicants.objects.filter(pk=val).update(BIB=BIb,chipcode1=chip1,chipcode2=chip2)
        print("y=",Y)
   
    return render(request, 'show.html', {'message': "registered"})