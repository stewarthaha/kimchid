"""kimchi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from kimchi import views as MyAppView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mypage/', MyAppView.DisplayMypage),
    path('blog/',include('blog.urls')),
    path('',include('blog.urls')), #url(r'', include('blog.urls'))에서 내가 수정함.
]
