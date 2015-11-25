from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = patterns ('',
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^', include("apps.login.urls")),
	url(r"^events/", include("apps.events.urls")),
    url(r'^admin/', admin.site.urls),
)
