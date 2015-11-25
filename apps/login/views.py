from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
import requests, json
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

	context = {
		'user': user,
	}	


	# url = "https://api.locu.com/v1_0/venue/search/?locality=Bellevue&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	# restaurants = {
	# 	"restaurants": json.loads(requests.get(url).content)
	# 	}
	# try:
	# 	request.session["city"]
	# except:
	# 	request.session["city"] = "Seattle"
	# city = request.session["city"]
	# url2 = "https://api.locu.com/v1_0/venue/search/?locality="+city+"&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"

	# context = {
	# 	'user': user,
	# 	'places': json.loads(requests.get(url2).content)
	# }	


	return render(request, 'login/home.html', context)

def logout(request):
	auth_logout(request)
	request.session.clear()
	return redirect('/')
