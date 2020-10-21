from django.shortcuts import render, HttpResponse
from .models import User


# Create your views here.
def homeview(request):
	return render(request, "index.html")

def displaycustomers(request):
	users = User.objects.all()
	context = {'users': users}
	return render(request, "viewcustomers.html", context)

def transferview(request):
	return render(request, 'transfer.html')
    


