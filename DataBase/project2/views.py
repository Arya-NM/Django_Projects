#from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from .models import employee

# Create your views here.


@login_required
def home(request):
	return render( request, 'base.html')

@login_required
def addperson(request):
	responseDic = {}
	try:
		Name = request.POST['name']
		Adderess = request.POST['address']

		emplist = employee(name=Name,address=Adderess)
		emplist.save()
		responseDic["msg1"]="Employee Added"
		return render(request, "sample.html", responseDic)

	except Exception as e:
		 print(e)
		 responseDic["msg1"]="Employee cannot be Added"
		 return render(request, "base.html", responseDic)

def sign_up(request):
	form = UserCreationForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			form.save()
			username = form.cleaned_data('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username,password=password)
			login(request,user)
			return redirect('login')
	else:
		form = UserCreationForm()
	return render(request, 'registration/signup.html',{'form':form})


def loginview(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request,user)
		return redirect('/')
	else:
		return render(request,"login.html")

def logout_view(request):
	logout(request)
	return redirect('login')	




