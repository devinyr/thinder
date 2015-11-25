from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.http import Http404
from django.contrib import messages
from models import *
import string

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

def profile(request):
	user = User.objects.get(id=request.session['user_id'])
	context = {'user': user}
	return render(request, 'login/profile.html', context)

def edit_profile(request):
	user = User.objects.get(id=request.session['user_id'])
	context = {'user': user}
	return render(request, 'login/edit_profile.html', context)

def update_profile(request):
	if request.method != 'POST':
		raise Http404('Invalid HTTP method!')
	go_back = False
	if len(request.POST['first_name']) < 1:
		messages.add_message(request, messages.INFO, 'First name cannot be empty!')
		go_back = True
	if len(request.POST['last_name']) < 1:
		messages.add_message(request, messages.INFO, 'Last name cannot be empty!')
		go_back = True
	if len(request.POST['email']) < 1:
		messages.add_message(request, messages.INFO, 'Email cannot be empty!')
		go_back = True
	if (request.POST['location'] != 'None') and (not request.POST['location'].isdigit()):
		messages.add_message(request, messages.INFO, 'Location must be a valid zip code (numbers only)!')
		go_back = True
	if go_back:
		return redirect('/profile/edit')
	else:
		user = User.objects.get(id=request.session['user_id'])
		user.first_name = request.POST['first_name']
		user.last_name = request.POST['last_name']
		user.email = request.POST['email']
		if request.POST['location'] != 'None':
			user.location = request.POST['location']
		user.save()
		return redirect('/profile')

def logout(request):
	auth_logout(request)
	request.session.clear()
	return redirect('/')
