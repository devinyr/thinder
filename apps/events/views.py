from django.shortcuts import render, redirect
import requests, json

def index(request):
	url = "https://api.locu.com/v1_0/venue/search/?locality=Bellevue&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	restaurants = {
		"restaurants": json.loads(requests.get(url).content)
		}
	try:
		request.session["city"]
	except:
		request.session["city"] = "Seattle"
	city = request.session["city"]
	url2 = "https://api.locu.com/v1_0/venue/search/?locality="+city+"&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	places = {
		"places": json.loads(requests.get(url2).content)
		}
	return render(request, "events/index.html", places)
def get_city(request):
	request.session["city"] = request.POST["city"]
	print request.session["city"]
	return redirect("/events/")
def show(request):
	return render(request, "events/show.html")

def create(request):
	return render(request, "events/create.html")
