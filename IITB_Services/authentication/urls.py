from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signin,name='home'),
    path('signup',views.signup,name='signup'),
    #path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('base',views.base,name='base'),
    path('welcome',views.afterlogin,name='afterlogin'),
    path('grocery',views.grocery,name='grocery'),
    path('grocery_h10',views.grocery_h10,name='grocery_h10'),
    path('gulmohar',views.gulmohar,name="gulmohar"),
    path('gulmohar_updation',views.gulmohar_updation,name="gulmohar_updation"),
    path('toggle',views.toggle,name="toggle"),
    path('hair',views.hair,name='hair'),
    path('hairsalon_admin',views.hairsalon_admin,name="hairsalon_admin"),
    path('orderDone', views.orderDone , name='orderDone'),
    path('order', views.order , name='order'),
    path('ordercompletion',views.ordercompletion,name="ordercompletion"),
    path('hoggle',views.hoggle,name='hoggle')
]