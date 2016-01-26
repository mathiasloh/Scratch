from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
	welcome_user = 'Welcome'
	context = {
		"welcome": welcome_user,
	}


	return render(request, 'index.html', context)