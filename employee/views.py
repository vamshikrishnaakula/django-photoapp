from sre_constants import SUCCESS
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
import os
from PIL import Image
import base64
import cv2
from imutils import paths
import cv2,os,re


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
        global res1 
        res1=res.upper() 
        print("res1==",res1)
        token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        print("token===",token)
        applicant = Applicants.objects.get(pk=val)
        candidate_data = candidate_photo.objects.get(pk=val)
        return render(request,'working_trail.html',{'result': applicant,'result_photo': candidate_data})
        # return render(request,'working_trail.html',{'result': applicant})
def chipdata(request):
        # num = 10 # define the length of the string   
        # res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
        # global res1 
        # res1=res.upper() 
        # print("res1==",res1)
        # token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        # print("token===",token)
        # applicant = Applicants.objects.get(pk=val)
        # candidate_data = candidate_photo.objects.get(pk=val)
    if request.method == 'POST':
        BiB=request.POST.get('BiB')
        print("prod.BIb=",BiB)
        Chipcode1=request.POST.get('Chipcode1')
        print("prod.chipcode1=",Chipcode1)
        Chipcode2=request.POST.get('Chipcode2')
        print("prod.chipcode1=",Chipcode2)
        message= "registered"
        imagedata=request.POST.get("src")
        new_data = imagedata.split(',')[-1]
        res = bytes(new_data, 'utf-8')
        print(" res====",type( res))
        base64data=base64.b64decode(res)
        """ blur detection code """
        def variance_of_laplacian(image):
                    return cv2.Laplacian(image, cv2.CV_64F).var()
        f0ggy=open("D:/Django-crud-application-master/images/"+ val+".jpg","wb")
        f0ggy.write(base64data)
        f0ggy.close()

        # dir_path = ("D:/Django-crud-application-master/images/"+"44"+".jpg")
        # dir_path = (base64data)
        # dir_path=("D:/facesblur/face (3).jpg")
        threshold = 250.0
        #
        # #
        #
        image = cv2.imread("D:/Django-crud-application-master/images/"+ val+".jpg")
        # print("image type is=======",image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fm = variance_of_laplacian(gray)
        print("this is the variance type=====", int(fm), fm)
        text = "Not Blurry"
        if fm < threshold:
                    print(fm)
                    text = "Blurry"
                    """take the picture again """
                    message = " photo is not clear"
                    return HttpResponse({"message":message})

        else:
            print(fm)
            print("this is at notBlur_per=")
            '''save into DB'''
            chipdata=Applicants.objects.filter(pk=val).update(BIB=BiB,chipcode1=Chipcode1,chipcode2=Chipcode2)
            print("chipdata=",chipdata)
            candidate_image = candidate_photo.objects.filter(pk=val).update(candidate_photo=imagedata)
            print("candidate_image===",candidate_image)
            cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            cv2.imshow("Image", image)
            key = cv2.waitKey(0)
        return render(request,'working_trail.html')
        #  return render(request,'working_trail.html')'result_photo': candidate_data

          
           

def update_data(request):
   
    if request.method == 'POST':
       
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
        
        # candidate_data = candidate_photo.objects.get(pk=val)
        return render(request,'working_trail.html')

def token_gen(request):
        # num = 10 # define the length of the string   
        # res = ''.join(secrets.choice(string.ascii_letters + string.digits) for x in range(num))
        # global res1 
        # res1=res.upper() 
        # print("res1==",res1)
        # token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        # print("token===",token)
        candidate_data = candidate_photo.objects.get(pk=val)
        """it suppose to genertate token """
        return render(request,'homepage.html',{'result_photo': candidate_data})

def showImage(request):
     candidate_image = candidate_photo.objects.get(pk=val)
     return render(request,'showimage.html',{"result_photo": candidate_image})

   