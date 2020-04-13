from django.shortcuts import render
from form.models import info

def home(request):
	if request.method=='POST':
		firstname=request.POST['first_name']
		lastname=request.POST['last_name']
		email=request.POST['email']
		message=request.POST['message']

		print(firstname,lastname,email,message)

		infoform=info(firstname=firstname,lastname=lastname,email=email,message=message)
		infoform.save()
        

	return render(request,'index.html')

def dash(request):
	return render(request,'dashboard.html')

