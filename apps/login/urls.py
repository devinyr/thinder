from django.conf.urls import include, url, patterns
import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^logout$', views.logout, name='logout'),
	url(r'^home$', views.home, name='home'),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
	url(r'^profile/update$', views.update_profile, name='update_profile'),
)
