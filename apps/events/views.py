from django.shortcuts import render, redirect
import requests, json

def index(request):
	pass

def get_city(request):
	request.session['city'] = request.POST["city"]
	url = "https://api.locu.com/v1_0/venue/search/?locality="+request.session['city']+"&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	places = {
		"places": json.loads(requests.get(url).content)
		}
	return render(request, "events/create.html", places)

def show(request):
  pass

def create(request):
	return render(request, 'events/create.html')
