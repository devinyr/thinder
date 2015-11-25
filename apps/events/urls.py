from django.conf.urls import include, url, patterns
from apps.events import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name="events_index"),
	url(r'^show/', views.show, name="show"),
	url(r'^create/', views.create, name="create"),
	url(r'^city/', views.get_city, name="city")
)