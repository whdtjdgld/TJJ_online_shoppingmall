"""DJangoEx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from member import views as mv
from product import views
# 패키지 app 내의 html 걸어주는 곳 views로 감
urlpatterns = [
    path( "bracelet", views.bracelet, name="bracelet" ),
    path( "ring", views.ring, name="ring" ),
    path( "earring", views.earring, name="earring" ),
    path( "necklace", views.necklace, name="necklace" ),
    path( "login",  mv.login, name="login" ),
    path( "main",  mv.main, name="main" ),
    path( "join",  mv.join, name="join" ),
    path( "logout",  mv.logout, name="logout" ),
    path( "plist",  views.plist, name="plist" ),
    path( "login", mv.login, name="login" ),  
]