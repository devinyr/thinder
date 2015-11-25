from django.shortcuts import render
import requests

def index(request):
  url = "https://api.locu.com/v1_0/venue/search/?locality=Bellevue&region=Wa&open_at=2015-11-26&api_key=ba6050865a98a654d2fa32c1b823f5769000dd77"

  food = requests.get(url).content
  place = food[0]
  print place
  return render(request, "events/index.html", food)

def show(request):
  pass

def create(request):
  pass
