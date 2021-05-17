from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm


# Create your views here.
def index(request):
	custform=CustomerForm()
	return render(request,"index.html",{"form":custform})

def addcustomer(request):
	try:
		custform=CustomerForm()
		if request.method=="POST":
			custform=CustomerForm(request.POST)
			if custform.is_valid():
				custform.save()
		return render(request,'index.html',{'form':custform,"msg":"added"})
	except Exception as e:
		print(e)
		return HttpResponse("Error")


