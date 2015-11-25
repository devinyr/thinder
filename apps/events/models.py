from django.db import models

class Event(models.Model):
  name = models.CharField(max_length=50)
  has_menu = models.BooleanField
  resource_uri = models.CharField(max_length = 255)
  time = models.TimeField
  notes = models.CharField
  class Meta:
    db_table = 'events'
