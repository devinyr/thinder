from django.shortcuts import render, redirect
import requests, json
from apps.events.models import Event, Reservation
from apps.login.models import User

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
	try:
		request.session['resource_uri']
	except:

	print 'IN SHOW************'
	places = json.loads(requests.get(url).content)
	data = places.get("objects") #Array of restraunts
	uri_str = data[0].get("resource_uri") #Get first element need to modify
	print uri_str
	newurl = "https://api.locu.com" + uri_str + "?api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	context = {
		"newurl" : newurl,
	}
	print newurl
	return render(request, "events/show.html", context)

def add(request):
	try:
		del request.session['city']
	except:
		pass
	return render(request, 'events/create.html')

def create(request):
	print request.POST
	content = {
		'name' 					: request.POST['name'],
		'resource_uri'	:	request.POST['resource_uri']
	}
	print content
	return render(request, 'events/create_form.html', content)

def commit(request):
	event = Event(event_name=request.POST['event_name'], restaurant_name=request.POST['name'], resource_uri=request.POST['resource_uri'],time=request.POST['start'], notes = request.POST['notes'])
	event.save()
	event_pk = Event.objects.all().order_by('pk'[:1])
	request.session['event_id'] = event.id
	request.session['resource_uri'] = event.resource_uri
	print request.session['event_id']
	print request.session['resource_uri']
	return redirect('/events/make_reservation')

def make_reservation(request):
	event = Event.objects.get(id = request.session['event_id'])
	user = User.objects.get(id = request.session['user_id'])
	Reservation.objects.create(event=event, user=user)


	# should save event to db and redirect to show page with details. Sample menu items if available. (Need to hit api again with the resource uri)
	# event = Event.objects.create()
	return render(request, 'events/show.html')


