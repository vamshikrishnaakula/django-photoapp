
This project contains-
 - creating table using ORM
 - listing, fetching, editing and deleting data from and to database

# For step by step 

Prerequisites before using Django-
basic knowledge of python, html, css and 
Applications need to install- Python and python virtual environment

a. Download and Install python

b. Create virtual environment(pip should be installed(check version- pip --version))
Install either virtualenvwrapper or virtualenv(for more info goto- link)
install virtual environment- pip install virtualenv
Create virtual environment- virtualenv <virtual-env>
Now activate virtual env - cd <virtual-env>/Scripts/activate

c. Install Django using command -
pip install django
Check django version command-
	python -m django --version


To create a Django application that performs CRUD operations, follow the following steps.
1. Create a Project, using command- 
$ django-admin startproject crudexample  
2. Create an App, using command- 
$ python3 manage.py startapp employee  

3. Database Setup -
Create a database djangodb in mysql, and configure into the settings.py file of django project. See the example.
// settings.py
DATABASES = {  
    'default': {  
        'ENGINE': 'mssql',  
        'NAME': 'django',  
        'USER':'*****',  
        'PASSWORD':'mssql',  
        'HOST':'localhost',  
        'PORT':'1:8000'  
    }  
}  

4. Create a Model- example
Put the following code into models.py file.
// models.py
from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee"  
 

6. Create View Functions-example
// views.py
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  

Create your views here. 

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee}) 

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

7. Provide Routing
Provide URL patterns to map with views function.
// urls.py
from django.contrib import admin  
from django.urls import path  
from employee import views  
urlpatterns = [  
    path('admin/', admin.site.urls),
      path('', include('employee.urls')),
]  

8. Creating routing for employee urls
// employee/urls.py
from django.urls import path
from . import views

urlpatterns  examples = [
    path('', views.show),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]

9. Organize Templates

create a base template for all files- templates/base.html
To tell django about this file, do some changes in settings.py-
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

Create a templates folder inside the main project and create base.html file there-
// base.html
Now a create a templates folder inside employee app and create three (index, edit, show) html files inside the directory. files are-
// index.html
// show.html
//edit.html


10. Now create css, create a static/css folder in main directory parallel to manage.py and create a file style.css in it.
changes to do at the end of settings.py-
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

and now tell djnago about your css file, run command-
python manage.py collectstatic
(it will create a folder assets in main directory with your css file in it. You should run this command always after making changes in your css, js or images.)

	
11. Create Migrations
Create migrations for the created model employee, use the following command.
====> python manage.py makemigrations  
After migrations, execute one more command to reflect the migration into the database. But before it, mention name of app (employee) in INSTALLED_APPS of settings.py file.
// settings.py
INSTALLED_APPS = [  
    'django.contrib.admin',  
    'django.contrib.auth',  
    'django.contrib.contenttypes',  
    'django.contrib.sessions',  
    'django.contrib.messages',  
    'django.contrib.staticfiles',  
    'employee'  
]  

Run the command to migrate the migrations.
====> python manage.py migrate  

Now, our application has successfully connected and created tables in database. It creates 10 default tables for handling project (session, authentication etc) and one table of our model that we created.
See list of tables created after migrate command.

Run Server
To run server use the following command.
====> python manage.py runserver  

Access to the Browser
Access the application by entering localhost:8000/, it will show all the available employee records.
Initially, there is no record. So, it shows no record message. 

12. Accessing admin panel, for that you have to create a super user using command-
python manage.py createsuperuser
(than follow instructions)


====> Debugging/basic errors-

1. Ms SQL connection Error-
Solution-
django.core.exceptions.ImproperlyConfigured: Error loading MsSQLdb module.
install odbc errors?



2. 'static-files' is not a registered tag library
Solution-
It's due to upgrading to Django3.0, use as mentioned above.
use-
{% load static %}





# Django photo app for candidate regitration

requirements:-


Django ==2.1

gunicorn==20.1.0
absl-py==1.0.0
asgiref==3.4.1
astunparse==1.6.3
beautifulsoup4==4.11.1
cachetools==4.2.4
certifi==2021.10.8
charset-normalizer==2.0.12
crispy-forms-gds==0.2.4
cycler==0.11.0
dataclasses==0.8
distlib==0.3.4
Django==3.2.14
django-base64field==1.0
django-crispy-forms==1.13.0
django-pyodbc-azure==2.1.0.0
django-widget-tweaks==1.4.11
filelock==3.4.1
fire==0.1.2
gast==0.3.3
google-auth==1.35.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
greenlet==1.1.2
grpcio==1.46.1
gunicorn==20.1.0
h5py==2.10.0
idna==3.3
importlib-metadata==4.8.3
importlib-resources==5.4.0
imutils==0.5.4
joblib==1.1.0
Keras-Preprocessing==1.1.2
kiwisolver==1.3.1
lxml==4.8.0
Markdown==3.3.7
matplotlib==3.3.4
mssql-django==1.1.3
numpy==1.19.5
oauthlib==3.2.0
opencv-contrib-python==3.4.17.61
opt-einsum==3.3.0
packaging==21.3
pandas==1.1.5
peewee==2.8.8
Pillow==8.4.0
platformdirs==2.4.0
protobuf==3.19.4
pyasn1==0.4.8
pyasn1-modules==0.2.8
pymongo==4.1.1
PyMySQL==1.0.2
pyodbc==4.0.32
pyparsing==3.0.8
PyQt5==5.15.6
PyQt5-Qt5==5.15.2
PyQt5-sip==12.9.1
python-dateutil==2.8.2
pytz==2022.1
requests==2.27.1
requests-oauthlib==1.3.1
rsa==4.8
scikit-learn==0.19.1
scipy==1.4.1
sip==6.5.1
six==1.16.0
soupsieve==2.3.2.post1
SQLAlchemy==1.4.39
sqlparse==0.4.2
tensorboard==2.2.2
tensorboard-plugin-wit==1.8.1
tensorflow==2.2.0
tensorflow-estimator==2.2.0
termcolor==1.1.0
threadpoolctl==3.1.0
toml==0.10.2
typing_extensions==4.1.1
urllib3==1.26.9
virtualenv==20.14.1
virtualenvwrapper-win==1.2.7
Werkzeug==2.0.3
Workon==0.8.2
wrapt==1.14.1
zipp==3.6.0

