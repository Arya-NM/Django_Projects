from django.urls import path
from .import views

urlpatterns = [
path('',views.home, name="home"),
path('add',views.insert),
path('display',views.display),
path('update',views.updation),
path('delete',views.delete)
]