
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name="home"),
    path('accounts/login/', views.loginview,name="login"),
    path('accounts/signup/',views.sign_up),
    path('logout',views.logout_view),
    path('addperson',views.addperson),
    
]