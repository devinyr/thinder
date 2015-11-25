from django.conf.urls import patterns, url

from .views import DonateView, SuccessView

urlpatterns = patterns(
	'',
	url(r'^donate/$', DonateView.as_view(), name = 'donate'),
	url(r'^thank_you/$', SuccessView.as_view(), name = 'thank_you'),
)