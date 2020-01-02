"""workplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'test', include('patients.urls')),
    url(r'check', include('patients.urls')),
    url(r'patients', include('patients.urls')),
    url(r'staffs/', include('staffs.urls')),
    url(r'invest', include('clinic.urls')),
    url(r'signup', include('login.urls')),
    url(r'login', include('login.urls')),
    url(r'spec/', include('staffs.urls')),
    url(r'staffer/', include('staffs.urls')),
    url(r'', include('clinic.urls')),
       ]