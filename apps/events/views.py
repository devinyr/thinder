from django.shortcuts import render
import requests

def index(request):
	url = "https://api.locu.com/v1_0/venue/search/?locality=Bellevue&region=Wa&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	restaurants = {
		"restaurants": requests.get(url).content
		}
	return render(request, "events/index.html", restaurants)

def show(request):
	return render(request, "events/show.html")

def create(request):
	return render(request, "events/create.html")
