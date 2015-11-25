from django.conf.urls import include, url, patterns
import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^home$', views.home, name='home'),
)
