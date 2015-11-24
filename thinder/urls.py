from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = patterns ('',
	url(r'^', include("apps.login.urls")),
    url(r'^admin/', admin.site.urls),
)
