from email import message
from sre_constants import SUCCESS
from cryptography.fernet import Fernet
from  encryption1  import *
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .forms import NameForm
from .models import Applicants,Imagedata, candidate_photo
import sys
from subprocess import run,PIPE
from token_gen import *
import random   
import string  
import secrets
import base64
import os
from PIL import Image
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
import base64
import cv2
import numpy as np
from imutils import paths
import cv2,os,re
from django.template import RequestContext


def Homepage(request):
    return render(request, 'Homepage-2.html')
def contacts(request):
    return render(request,'contacts.html')
def updateinfo(request):
    return render(request,'updates.html')
def Home(request):

    return render(request,'Homepage-2.html')
def help(request):
    reg_count=Applicants.objects.exclude(BIB__isnull=True).count()
    print("reg_count",reg_count)
    Total_count=Applicants.objects.all().count()
    print("Total_count",Total_count)
    Remaining= Applicants.objects.exclude(BIB__isnull=False).count()
    print(int(Total_count) - int( reg_count))

    return render(request,'Dash_board.html',{'Total_count':Total_count,'reg_count':reg_count,'Remaining': Remaining})


def add1(request):
        global val
        val=request.POST.get('num2')
        valid=Applicants.objects.filter(pk=val).values_list('BIB')
        print("valid==",valid)
        for i in valid:
            
            for j in i:
              print("j==",j)
            if  j == None :

                    applicant = Applicants.objects.get(pk=val)
                    print("applicant==",applicant)
                    num = 10 # define the length of the string  
                    res = ''.join(secrets.choice( string.digits) for x in range(num)) 
                    res1=res.upper() 
                    print("res1==",res1)
                    token = candidate_photo.objects.filter(pk=val).update(token=res1 )
                    print("token===",token)
                    candidate_data = candidate_photo.objects.get(pk=val)
               
                    return render(request,'today-2.html',{'result': applicant,'result_photo': candidate_data})
                    
            else :
                    print(" This was registered already ")
                    messages.error(request, ' This was  registered already')
                    return render(request,'Homepage-2.html')
                    
        # return render(request,'today-2.html',{'result': applicant})   
def chipdata(request):
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
        # print(" res====",type( res))
        base64data=base64.b64decode(res)
        '''Encryption has to impliment'''
        # fernet = Fernet(key)
        # encrypted = fernet.encrypt(base64data)
        def variance_of_laplacian(image):
                    return cv2.Laplacian(image, cv2.CV_64F).var()
        
        f0ggy=open("D:/Django-crud-application-master/images/"+ val+".jpg","wb")
        f0ggy.write(base64data)
        # f0ggy.write(encrypted)
        # f0ggy.close()
        image1=open("D:/Django-crud-application-master/images/"+ val+".jpg","rb")
        image=image1.read()
        threshold = 350.0
        image = cv2.imread("D:/Django-crud-application-master/images/"+ val+".jpg")
        # image = cv2.imread(base64data)
        # image = cv2.imdecode(np.fromstring(base64data, np.uint8), cv2.IMREAD_COLOR)
        # print("image type is=======",type(image))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        print("faces",faces)
        if len(faces) !=0 :
                for (x,y,w,h) in faces :
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    faces = image[y:y + h, x:x + w]
                    fm = variance_of_laplacian(faces)
                    print("this is the variance type=====", int(fm), fm)
                    
                    if fm >= threshold:
                                print(fm)
                                chipdata=Applicants.objects.filter(pk=val).update(BIB=BiB,chipcode1=Chipcode1,chipcode2=Chipcode2)
                                print("chipdata=",chipdata)
                                # messages.add_message(request,messages.SUCCESS," photo is not clear ")
                                candidate_image = candidate_photo.objects.filter(pk=val).update(candidate_photo=imagedata)
                                print("candidate_image===",candidate_image)
                                text = "Not Blurry"
                                # cv2.putText(faces, "{}: {:.2f}".format(text, fm), (10, 30),
                                #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                                # cv2.imshow("Image",faces)
                                # key = cv2.waitKey(0)
                                # fernet = Fernet(key)
                                # encrypted = fernet.encrypt(bytes(image))
                                # # print("encrypted",encrypted)
                                # f0ggy.truncate(0)
                                # f = open("D:/Django-crud-application-master/images/"+ val+".jpg", "r+")
                                # f.write(str(encrypted))
                                # f.close()
                                # # fernet = Fernet(key)
                                # file2 = open("D:/Django-crud-application-master/images/"+ val+".jpg", "rb")
                                # encrypted_file = file2.read()
                                # # decrypted = fernet.decrypt(encrypted_file)
                                
                                # # file2.write(decrypted)
                                # f0ggy.close()
                                file = open('D:/Django-crud-application-master/images/'+ val+'.jpg', 'rb')
                                image=file.read()
                                # file.close()

                                image=bytearray(image)
                                key=230
                                for i ,j in enumerate(image):
                                    image[i] = j^key
                                file=open('D:/Django-crud-application-master/images/'+ val+'.jpg','wb')
                                file.truncate(0)
                                file.write(image)
                                file.close()

                                return render(request,'today-2.html')

                    else:
                            print(fm)
                            print("photo is not clear")
                            return render(request,'today-2..html')
        else:
            print("no face was detected")
            # return render(request,'working_trail.html')

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
    
        finger_print = candidate_photo.objects.filter(pk=val).update(ltiimagedata=ltiimage,rtiimagedata=rtiimage,lti_iso=lti_iso,rti_iso=rti_iso)
        print("finger_print===",finger_print)
        return render(request,'today-2.html')
        # return render(request,'working_trail.html')

def token_gen(request):

        candidate_data = candidate_photo.objects.get(pk=val)
        """it suppose to genertate token """
        return render(request,'homepage.html')
        # return render(request,'homepage.html',{'result_photo': candidate_data})

def showImage(request):
     candidate_image = candidate_photo.objects.get(pk=val)
     return render(request,'showimage.html',{"result_photo": candidate_image})

   