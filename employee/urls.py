"""DjangoJavaTpointCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin  
from django.urls import path  
from employee import views  
urlpatterns = [  
       path('', views.Homepage),
       path('Help', views.help),
       path('Home', views.ome),
       path('Updates', views.updateinfo,name='Updates'),
       path('Contacts', views.contacts,name='contacts'),
       path('add1',views.add1),
       path('chipdata',views.chipdata,name='chipdata'),
       path('photodata',views.photodata,name='photodata'),
       path('showImage',views.showImage,name='showImage'),
       path('update_fingerprints',views.update_fingerprints,name='update_fingerprints')
]  
