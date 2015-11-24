from django.conf.urls import include, url, patterns
import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name="index"),
)