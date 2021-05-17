from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'index.html')

def calcu(request):
	a = int(request.POST['numa'])
	b = int(request.POST['numb'])
	name = request.POST['cal']
	if name == 'add':
		result = a+b

	elif name == 'sub':
		result = a-b

	elif name == 'div':
		result = a/b

	elif name == 'mul':
		result = a*b

	return render(request, 'index.html',{
		"msg": result
		})
