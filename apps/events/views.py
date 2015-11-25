from django.shortcuts import render, redirect
import requests, json
# from apps.events import Event, Reservation

def index(request):
	return render(request, 'events/index.html')

def get_city(request):
	request.session['city'] = request.POST["city"]
	url = "https://api.locu.com/v1_0/venue/search/?locality="+request.session['city']+"&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	places = {
		"places": json.loads(requests.get(url).content)
		}
	return render(request, "events/create.html", places)

def show(request):
  pass

def add(request):
	del request.session['city']
	return render(request, 'events/create.html')

def create(request):
	print request.POST
	content = {
		'name' 					: request.POST['name'],
		'has_menu'			:	request.POST['has_menu'],
		'resource_uri'	:	request.POST['resource_uri']
	}
	print content
	return render(request, 'events/create_form.html', content)

def commit(request):
	# should save event to db and redirect to show page with details. Sample menu items if available. (Need to hit api again with the resource uri)
	# event = Event.objects.create()
	return render(request, 'events/show.html')


