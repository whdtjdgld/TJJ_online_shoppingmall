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
from board import views

urlpatterns = [
    path( "boardlist", views.boardlist, name="boardlist" ),
    path( "write", views.write, name="write" ),
    path( "writepro", views.writepro, name="writepro" ), 
    path( "detail", views.detail, name="detail" ),  
    path( "boardmodify", views.boardmodify, name="boardmodify" ),
    path( "boardview", views.boardview, name="boardview" ),
    path( "boarddelete", views.boarddelete, name="boarddelete" ),
]