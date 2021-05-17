from django.urls import path
from .import views

urlpatterns = [
path('',views.home, name="home"),
path('add',views.insert_bal),
path('display',views.display),
path('insert',views.add_bal)
]