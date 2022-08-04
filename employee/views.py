from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import JsonResponse
from .forms import NameForm
from .models import Applicants,Imagedata, candidate_photo
# global val

def Homepage(request):
    # stud=Employee.objects.get(pk=101)
    # val=request.GET['num1']
    return render(request, 'Homepage.html')
def contacts(request):
    return render(request,'contacts.html')
def updateinfo(request):
    return render(request,'updates.html')
def ome(request):
    return render(request,'Homepage.html')
def help(request):
    return render(request,'help.html')


def add1(request):
    global val
    val=request.POST.get('num2')
    print("val22=",val)
    stu = Applicants.objects.get(pk=val)
    print("stu==",stu)
    return render(request,'main.html',{'result': stu})
         
   
def chipdata(request):
    # val=request.POST.get('num2')

    print("val22=",val)
    # cand = Applicants.objects.get(pk=val)
   
    if request.method == 'POST':
        #print(request.POST)
        # form = EmployeeForm(request.POST, instance=employee)
        BiB=request.POST.get('BiB')
        print("prod.BIb=",BiB)
        Chipcode1=request.POST.get('Chipcode1')
        print("prod.chipcode1=",Chipcode1)
        Chipcode2=request.POST.get('Chipcode2')
        print("prod.chipcode1=",Chipcode2)
        if BiB and Chipcode1 and Chipcode2 :
            
            Y=Applicants.objects.filter(pk=val).update(BIB=BiB,chipcode1=Chipcode1,chipcode2=Chipcode2)
            print("y=",Y)
   
    return render(request, 'main.html', {'message': "registered"})
def photodata (request):
    print("val22=",val)
 
    if request.method == 'POST':
        # print("request===",request)
        imagedata=request.POST.get("src")
        #print("image=======",imagedata)
        
        obj = candidate_photo.objects.filter(pk=val).update(candidate_photo=imagedata)  # create a object of Image type defined in your model
        print("obj===",obj)
        # if imagedata  :
            
            # Y=Imagedata.objects.get(pk=val).update(imagedata=imagedata)
            # print("y=",Y)
    return render(request, 'main.html')
        
    
    
    # return render(request, 'trail.html', {'result': stu})
def showImage(request):
    candidate_image = candidate_photo.objects.get(pk=val)
    return render(request,'showimage.html',{"result_photo": candidate_image})

def update_fingerprints(request):
    if request.method == 'POST':
        print("its a update_fingerprint")
        ltiimage=request.POST.get("fingerprint")
        print("image=======",ltiimage)
        rtiimage=request.POST.get("imgFingerrti1")
        print("image=======",rtiimage)
        lti_iso=request.POST.get("txtIsoTemplate")
        print("image=======",lti_iso)
        rti_iso=request.POST.get("txtIsoImagerti")
        print("image=======",rti_iso)
        
        # finger_print = candidate_photo.objects.filter(pk=val).update(ltiimagedata=ltiimage,rtiimagedata=rtiimage,lti_iso=lti_iso,rti_iso=rti_iso)  # create a object of Image type defined in your model
        # print("finger_print===",finger_print)
        # if imagedata  :
            
            # Y=Imagedata.objects.get(pk=val).update(imagedata=imagedata)
            # print("y=",Y)
    return render(request, 'main.html', {'message': "registered"})