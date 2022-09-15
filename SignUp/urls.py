from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('sup',views.sup,name='signup_data'),
    path('login',views.login,name='login'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('loginHandle',views.loginHandle,name='loginHandle'),
    path('home',views.home,name='home'),
    # path('aboutus',views.aboutus,name='aboutus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('adminloginHandle',views.adminloginHandle,name='adminloginHandle'),
    path('adminlogout',views.adminlogout,name='adminlogout'),

    
]

