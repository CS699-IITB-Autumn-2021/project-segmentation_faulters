from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='home'),
    path('signup',views.signup,name='signup'),
    #path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('base',views.base,name='base'),
    path('welcome',views.afterlogin,name='afterlogin')

]