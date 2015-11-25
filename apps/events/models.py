from django.db import models
from apps.login.models import User
class Event(models.Model):
	event_name = models.CharField(max_length=100)
	restaurant_name = models.CharField(max_length=50)
	resource_uri = models.CharField(max_length = 255)
	time = models.TimeField
	notes = models.CharField
	class Meta:
		db_table = 'events'

class Reservation(models.Model):
	event = models.ForeignKey(Event)
	user = models.ForeignKey(User)
	class Meta:
		db_table = 'reservations'