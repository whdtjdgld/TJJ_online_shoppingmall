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
from order import views
# 패키지 app 내의 views 걸어주는 곳
urlpatterns = [
    path( "logout", mv.logout, name="logout" ),
    path( "mypage", mv.mypage, name="mypage" ),
    path( "cart", views.cart, name="cart" ),
    path( "join", mv.join, name="join" ),
    path( "login", mv.login, name="login" ),
    path( "main", mv.main, name="main" ),
    path( "confirm", mv.confirm, name="confirm" ),
    path( "cart_view", views.cart_view, name="cart_view" ),
    path( "del_cart", views.del_cart, name="del_cart" ),   
    path( "del_cart_pro", views.del_cart_pro, name="del_cart_pro" ),
    path( "add_cart", views.add_cart, name="add_cart" ),
    path( "add_cart_pro", views.add_cart_pro, name="add_cart_pro" ),
    path( "minus_cart", views.minus_cart, name="minus_cart" ),
    path( "minus_cart_pro", views.minus_cart_pro, name="minus_cart_pro" ),
    path( "orderlist", mv.orderlist, name="orderlist" ),
    path( "buy_pro", views.buy_pro, name="buy_pro" ),
    path( "buy", views.buy, name="buy" ),

]