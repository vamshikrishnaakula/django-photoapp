from sre_constants import SUCCESS
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .forms import NameForm
# from django.contrib import messages
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
from django.template import RequestContext


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
             
        applicant = Applicants.objects.get(pk=val)
        print("applicant==",applicant)
        # mydata = Applicants.objects.values_list('pk')
        # # print("mydata===",mydata)
        # for num in Applicants.objects.all():
        #         print("num====",num)
        # #   if applicant in num:
        num = 10 # define the length of the string   
        res = ''.join(secrets.choice( string.digits) for x in range(num)) 
        res1=res.upper() 
        print("res1==",res1)
        token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        print("token===",token)
        candidate_data = candidate_photo.objects.get(pk=val)
        return render(request,'working_trail.html',{'result': applicant,'result_photo': candidate_data})   
        # res1=res.upper() 
        #         print("res1==",res1)
        #         token = candidate_photo.objects.filter(pk=val).update(token=res1 )
        #         print("token===",token)
        #         candidate_data = candidate_photo.objects.get(pk=val)
        #         return render(request,'working_trail.html',{'result': applicant,'result_photo': candidate_data})   
        #             # return render(request,'working_trail.html',{'result': applicant})          
        # # else:
        #         print("no record found")
        #         return render(request,"Homepage.html")
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
        threshold = 350.0
        image = cv2.imread("D:/Django-crud-application-master/images/"+ val+".jpg")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        print("faces",faces)
        if len(faces) !=0 :
            for (x,y,w,h) in faces :
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                faces = image[y:y + h, x:x + w]
                # print("faces==2",faces)
                fm = variance_of_laplacian(faces)
                print("this is the variance type=====", int(fm), fm)
                text = "Not Blurry"

                if fm >= threshold:
                    print(fm)
                    print("this is at notBlur_per=")
                    '''save into DB'''
                    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.imshow("Image", faces)
                    key = cv2.waitKey(0)
                    chipdata=Applicants.objects.filter(pk=val).update(BIB=BiB,chipcode1=Chipcode1,chipcode2=Chipcode2)
                    print("chipdata=",chipdata)
                    candidate_image = candidate_photo.objects.filter(pk=val).update(candidate_photo=imagedata)
                    print("candidate_image===",candidate_image)
                    
                    return render(request,'working_trail.html')
                else:
                    print(fm)
                    text = "Blurry"
                    print(" photo is not clear")
                    """take the picture again """
                    # mesages.error(request, 'photo is not clear')
                    return render(request,'working_trail.html')
                    # return redirect("add1")
        else:
            print("no faces were detected")
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

   