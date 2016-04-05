from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import UserProfile, Games
from .forms import GameForm

# Create your views here.
def home(request):


	welcome_user = 'Welcome'
	context = {
		"welcome": welcome_user,
	}

	if request.user.is_authenticated:
		queryset = UserProfile.objects.all()
		# loginid = queryset.username
		# HttpResponseRedirect('/%s/'%loginid) 
		for obj in queryset:
			if obj.username == request.user.username:
				return HttpResponseRedirect(reverse('user_index', args = [request.user.username]))
	


	return render(request, 'index.html', context)

def AlreadyAdded(user, gamelist):
	count = 0
	for items in gamelist:
		if user == items.users:
			count += 1
	if count == 0:
		return False
	return True

def getGame(user, gamelist):
	for item in gamelist:
		if user == item.users:
			return item

def home_user(request, username):
	user_object = UserProfile.objects.get(username=username)
	gamelist = Games.objects.all()
	if not AlreadyAdded(user_object, gamelist):
		games = Games(users=user_object)

	for items in gamelist:
		print(items.users.username)

	if request.user.is_authenticated:
		queryset = UserProfile.objects.all()
		queryset = sorted(queryset, key=lambda x: x.stars, reverse=True)
		context = {
			"userobject": user_object,
			"queryset" : queryset
		}

	return render(request, 'index_user.html', context)
 
def play_user(request, username):
	user_object = UserProfile.objects.get(username=username)
	games = getGame(user_object, Games.objects.all())
	SECRETCODE = "bonbon"
	if request.user.is_authenticated:
		form = GameForm()
		if request.method == 'POST':
			form = GameForm(request.POST or None)
			if form.is_valid():
				cd = form.cleaned_data
				code = cd.get('code')
				form = GameForm()
		
			if code == SECRETCODE:
				if not games.game1:
					games.game1 = True
					games.save()
					user_object.stars += 10
					user_object.save()

		queryset = UserProfile.objects.all()
		context = {
			"userobject": user_object,
			"queryset" : queryset,
			"form": form,
			"games": games,
		}

	return render(request, 'play.html', context)

def tuto_user(request, username):
	user_object = UserProfile.objects.get(username=username)
	games = getGame(user_object, Games.objects.all())
	SECRETCODE = "bonbon"

	if request.user.is_authenticated:
		form = GameForm()
		if request.method == 'POST':
			form = GameForm(request.POST or None)
			if form.is_valid():
				cd = form.cleaned_data
				code = cd.get('code')
				form = GameForm()

			if code == SECRETCODE:
				if not games.tutorial:
					games.tutorial = True
					games.save()
					user_object.stars += 5
					user_object.save()

		queryset = UserProfile.objects.all()
		queryset = sorted(queryset, key=lambda x: x.stars, reverse=True)
		context = {
			"userobject": user_object,
			"queryset" : queryset,
			"form": form,
			"games": games,
		}

	return render(request, 'tuto.html', context)

def summary_user(request, username):
	user_object = UserProfile.objects.get(username=username)
	games = getGame(user_object, Games.objects.all())

	if request.user.is_authenticated:
		queryset = UserProfile.objects.all()
		queryset = sorted(queryset, key=lambda x: x.stars, reverse=True)
		context = {
			"userobject": user_object,
			"queryset" : queryset,
			"games" : games
		}

	return render(request, 'summary.html', context)
