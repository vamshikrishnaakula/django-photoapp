from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .forms import NameForm
from .models import Applicants,Imagedata, candidate_photo
import sys
from subprocess import run,PIPE
# import token_gen.py
from token_gen import *
import random   
import string  
import secrets
import base64


def Homepage(request):
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
        num = 10 # define the length of the string   
        res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num)) 
        res1=res.upper() 
        print("res1==",res1)
        token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        print("token===",token)
        applicant = Applicants.objects.get(pk=val)
        candidate_data = candidate_photo.objects.get(pk=val)
        return render(request,'show.html',{'result': applicant,'result_photo': candidate_data})
def update_data(request):
   
    if request.method == 'POST':
        BiB=request.POST.get('BiB')
        print("prod.BIb=",BiB)
        Chipcode1=request.POST.get('Chipcode1')
        print("prod.chipcode1=",Chipcode1)
        Chipcode2=request.POST.get('Chipcode2')
        print("prod.chipcode1=",Chipcode2)
        message= "registered"
      
        chipdata=Applicants.objects.filter(pk=val).update(BIB=BiB,chipcode1=Chipcode1,chipcode2=Chipcode2)
        print("chipdata=",chipdata)

        # print("request===",request)
        imagedata=request.POST.get("src")
        #print("image=======",imagedata)
        candidate_image = candidate_photo.objects.filter(pk=val).update(candidate_photo=imagedata)
        print("candidate_image===",candidate_image)
        ltiimage=request.POST.get("imgFinger1")
        #print("ltiimage=======",ltiimage)
        rtiimage=rtiimage=request.POST.get("imgFingerrti1")
        #print("rtiimage=======",rtiimage)
        lti_iso=request.POST.get("txtIsoImage")
        #print("lti_iso=======",lti_iso)
        rti_iso=request.POST.get("txtIsoImagerti")
        #print("rti_iso=======",rti_iso)
        message="updated successfully"
        #---------image processing pending------------------------#
    
        finger_print = candidate_photo.objects.filter(pk=val).update(ltiimagedata=ltiimage,rtiimagedata=rtiimage,lti_iso=lti_iso,rti_iso=rti_iso)
        print("finger_print===",finger_print)
        #return render(request, 'main.html')
        # num = 10 # define the length of the string   
        # res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num)) 
        # res1=res.upper() 
        # print("res1==",res1)
        # token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        # print("token===",token)
        feild = candidate_photo.objects.get(pk=val)
        print("feild==",feild)
        return render(request,'show.html',{'result_photo':feild})
        #return render(request, 'test.html',{'data2':feild})

# def token_gen(request):
#         global val
#         feild = candidate_photo.objects.get(pk=val)
#         print("feild==",feild)
#         return render(request,'show.html',{'result_photo':feild})
# #   return render(request,'main.html',{'data1':str(res1)})
def showImage(request):
    candidate_image = candidate_photo.objects.get(pk=val)
    return render(request,'showimage.html',{"result_photo": candidate_image})

   