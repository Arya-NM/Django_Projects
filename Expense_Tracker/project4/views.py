from django.shortcuts import render
from django.db import models
from .models import expance,initial_balance

# Create your views here.

def home(request):
	return render(request, 'index.html')

def add_bal(request):
	responseDic={}
	in_bal=int(request.POST['ini_bal'])
	value=initial_balance.objects.filter(id=1).exists()
	if(value==True):
		val=initial_balance.objects.get(id=1)
		old_val=val.initial_bal
		new_val=old_val+in_bal
		val.initial_bal=new_val
		val.save()
		responseDic["msg"]="balance updated"
		return render(request,'index.html',{"msg":"balance updated"})
	else:
		culist=initial_balance(initial_bal=in_bal)
		culist.save()
		responseDic["msg"]="initial balance added"
		return render(request,'index.html',{"msg":"initial balance added"})

def insert_bal(request):
	responseDic={}
	Name=request.POST['iname']
	Amd=int(request.POST['amd'])
	value=initial_balance.objects.get(id=1)
	new_in=value.initial_bal
	if(new_in>Amd):
		clist=expance.objects.filter(expance_name=Name).exists()
		if(clist==True):
			itemlist=expance.objects.get(expance_name=Name)
			old_value=itemlist.expance_amount
			new_value=old_value+Amd
			itemlist.expance_amount=new_value
			itemlist.save()
			new_in_val=new_in-Amd
			value.initial_bal=new_in_val
			value.save()
			responseDic["msg"]="initial balance updated"
			return render(request,"index.html",{"msg":"initial balance updated"})
		else:
			culist=expance(expance_name=Name,expance_amount=Amd)
			culist.save()
			va=initial_balance.objects.get(id=1)
			n_in=value.initial_bal
			new_in_val=n_in-Amd
			va.initial_bal=new_in_val
			va.save()
			responseDic["msg"]="initial balance updated"
			return render(request,"index.html",{"msg":"initial balance updated"})
	else:
		responseDic["msg"]="balance infuss"
		return render(request,"index.html",{"msg":"balance infuss"})




def display(request):
	cudtls=expance.objects.all()
	return render(request,"index.html",{'cudtls':cudtls})
