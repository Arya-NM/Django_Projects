from django.shortcuts import render
from django.db import models
from .models import contact

# Create your views here.

def home(request):
	return render(request, 'index.html')


#addcontact
def insert(request):
	responseDic={}
	try:
		Name = request.POST['name']
		phn_num =int(request.POST['phone_number'])
		clist = contact.objects.filter(name=Name).exists()

		if(clist==True):
				responseDic["msg2"]="contact name already exists"
				return render(request,"index.html",responseDic)
		else:
			culist=contact(name=Name,phone_number=phn_num)
			culist.save()
			responseDic["msg1"]="contact add"
			return render(request,"index.html",responseDic)


	except Exception as e:
		print(e)
		responseDic["msg3"]="contact cannot be Added"
		return render(request,"index.html",responseDic)


#update contact 
def updation(request):
	responseDic={}
	n1=(request.POST["name"])
	n2=(request.POST["phone_number"])
	nn=(request.POST["newname"])
	np=(request.POST["newnum"])
	new=request.POST["btn"]

	if(new=="chgnum"):
		clist=contact.objects.filter(phone_number=n2).exists()
		if(clist==True):
			culist=contact.objects.get(phone_number=n2)
			culist.phone_number=np
			culist.save()
			responseDic["msg3"]="num updation"
			return render(request,"index.html",{"msg":"num changed"})
	elif(new=="chgname"):
		clist=contact.objects.filter(name=n1).exists()
		if(clist==True):
			culist=contact.objects.get(name=n1)
			culist.name=nn
			culist.save()
			responseDic["msg3"]="name updated"
			return render(request,"index.html",{"msg":"name changed"})

def display(request):
	cudtls=contact.objects.all()
	return render(request,"index.html",{'cudtls':cudtls})
	
def delete(request):
	name=request.POST['name']
	cudtls=contact.objects.filter(name=name)
	cudtls.delete()
	return render(request,"index.html",{'msg':"name delete"})



