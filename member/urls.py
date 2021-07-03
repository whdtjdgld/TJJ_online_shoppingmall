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
from member import views
from board import views as bv

# 패키지 app 내의 html 걸어주는 곳 views로 감
urlpatterns = [
    path( "logout", views.logout, name="logout" ),
    path( "mypage", views.mypage, name="mypage" ),
    path( "join", views.join, name="join" ),
    path( "login", views.login, name="login" ),
    path( "main", views.main, name="main" ),
    path( "confirm", views.confirm, name="confirm" ),
    path( "mypage", views.mypage, name="mypage" ),
    path( "modify", views.modify, name="modify" ),
    path( "modifypro", views.modifypro, name="modifypro" ),
    path( "emailcheck", views.emailcheck, name="emailcheck" ),
    path( "delete", views.delete, name="delete" ),
    path( "orderlist", views.orderlist, name="orderlist" ),
    path( "boardlist", bv.boardlist, name="boardlist" ),
    path( "write", bv.write, name="write" ),
    path( "writepro", bv.writepro, name="writepro" ), 
    path( "detail", bv.detail, name="detail" ),  
    path( "boardmodify", bv.boardmodify, name="boardmodify" ),
    path( "boardview", bv.boardview, name="boardview" ),
    path( "boarddelete", bv.boarddelete, name="boarddelete" ),
    path("",views.main, name="main")
]