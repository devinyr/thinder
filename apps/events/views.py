from django.shortcuts import render, redirect
import requests, json
from apps.events.models import Event, Reservation
from apps.login.models import User

def index(request):
	return render(request, 'events/index.html', context)

def redirected_home(request):
	if User.objects.filter(email=request.user.email).count() > 0:
		user = User.objects.get(email=request.user.email)
	else:
		user = User(first_name=request.user.first_name, last_name=request.user.last_name, username=request.user.username, email=request.user.email, last_login=request.user.last_login)
		user.save()
	request.session['user_id'] = user.id
	request.session["user_firstname"] = user.first_name
	my_reservations = Reservation.objects.filter(user=user)
	events = []
	for reservation in my_reservations:
		event = Event.objects.get(id=reservation.event.id)
		events.append(event)
	other_reservations = Reservation.objects.exclude(user=user)
	other_events = []
	for reservation in other_reservations:
		event = Event.objects.get(id=reservation.event.id)
		other_events.append(event)
	context = {'my_reservations': events, 'other_events': other_events, 'user': user}
	return render(request, 'events/index.html', context)

def get_city(request):
	request.session['city'] = request.POST["city"]
	url = "https://api.locu.com/v1_0/venue/search/?locality="+request.session['city']+"&region=Wa&category=restaurant&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"
	places = {
		"places": json.loads(requests.get(url).content)
		}
	return render(request, "events/create.html", places)

def show(request):
	uri_str = request.session['resource_uri'] #Get first element need to modify
>>>>>>> dev_mck
	print uri_str
	newurl = "https://api.locu.com" + uri_str + "?api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"

	content = {
		"event": json.loads(requests.get(newurl).content)
		}
	print content

	return render(request, "events/show.html", content)

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
	return render(request, 'events/create_form.html', content)

def commit(request):
	event = Event(event_name=request.POST['event_name'], restaurant_name=request.POST['name'], resource_uri=request.POST['resource_uri'],time=request.POST['start'], notes = request.POST['notes'])
	event.save()
	event_pk = Event.objects.all().order_by('pk'[:1])
	request.session['event_id'] = event.id
	request.session['resource_uri'] = event.resource_uri
	request.session['event_name'] = event.event_name
	request.session['notes'] = event.notes
	return redirect('/events/make_reservation')

def make_reservation(request):
	event = Event.objects.get(id = request.session['event_id'])
	user = User.objects.get(id = request.session['user_id'])
	Reservation.objects.create(event=event, user=user)


	# should save event to db and redirect to show page with details. Sample menu items if available. (Need to hit api again with the resource uri)
	# event = Event.objects.create()
<<<<<<< HEAD
	return render(request, 'events/show.html')
=======
	return redirect('/events/show')


>>>>>>> dev_mck
