from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from models import *

def index(request):
	return render(request, 'login/index.html')

def home(request):
	if User.objects.filter(email=request.user.email).count() > 0:
		user = User.objects.get(email=request.user.email)
	else:
		user = User(first_name=request.user.first_name, last_name=request.user.last_name, username=request.user.username, email=request.user.email, last_login=request.user.last_login)
		user.save()
	request.session['user_id'] = user.id
	request.session["user_firstname"] = user.first_name 
	context = {'user': user}
	return render(request, 'events/index.html', context)

def logout(request):
	auth_logout(request)
	request.session.clear()
	return redirect('/')
