"""employedatapro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from employedataapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.employedataView),
    path('fetch_all',views.fetchingalldata),
    path('',views.mainpage),
    path('mainpage', views.mainpage, name='mainpage'),
    path('hydrabad',views.hydrabaddata, name='hydrabad'),
    path('banglore',views.bangloredata, name='banglore'),
    path('chennai',views.chennaidata, name='chennai'),
    path('pune',views.punedata, name='pune')
]
