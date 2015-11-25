from django.conf.urls import include, url, patterns
from apps.events import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name="events_index"),
	url(r'^show/', views.show, name="show"),
	url(r'^add', views.add, name="add"),
	url(r'^city/', views.get_city, name="city"),
  url(r'^create', views.create, name='create'),
  url(r'^commit', views.commit, name='commit'),
  url(r'^make_reservation', views.make_reservation, name='reservation'),
)
