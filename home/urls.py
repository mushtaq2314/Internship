"""Internship URL Configuration

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
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name='home'),
    path('index.html',views.index,name='home'),
    path('admin.html',views.admin,name='admin'),
    path('login.html',views.login,name='login'),
    path('signup.html',views.signup,name='signup'),
    path('dashboard.html',views.dashboard,name='dashboard'),
    path('done.html',views.done,name='done'),
    path('contact.html',views.contact,name='contact'),
    path('adminlogin.html',views.adminlogin,name='adminlogin'),
    path('previous.html',views.previous,name='previous'),

]
