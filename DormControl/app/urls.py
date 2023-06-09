"""
URL configuration for DormControl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.studentLogin, name='studentLogin'),
    path('logout/', views.logout_view, name='logoutview'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('download/', views.download_file),
    path('mess/', views.mess, name='mess'),
    path('adminfront/', views.adminfront, name='adminfront'),
    path('complaints/', views.complaints, name='complaints'),
    path('checkInOut/', views.checkInOut, name='checkInOut  '),
    path('gatepassdetails/', views.gatepassdetails, name='gatepassdetails'),
    path('complaintsdetails/', views.complaintsdetails, name='complaintsdetails'),
    path('studentdetails/', views.studentdetails, name='studentdetails'),
]
