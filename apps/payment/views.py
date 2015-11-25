
import stripe
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import StripeForm

#Mixins are special kinds of multiple inheritance. 
#They are used when we want to provide optional features in a class
#They are also used to implement a particular feature in different classes.
#In our case, we use it to access the publishable key and use it in any class we need.
#We used the Mixin in our DonateView because that is where the keys will be used
class StripeMixin(object):
	def get_context_data(self, **kwargs):
		context = super(StripeMixin, self).get_context_data(**kwargs)
		context = {'publishable_key': settings.STRIPE_PUBLIC_KEY}
		return context

class SuccessView(TemplateView):
	template_name = 'payment/thank_you.html'

#Inherits the Mixin class from StripeMixin
class DonateView(StripeMixin,FormView):
	print '==================='
	template_name = 'payment/donate.html'
	form_class = StripeForm
	print '&&&&&&&&&&&&&&&&&&&'
	success_url = reverse_lazy('thank_you')


	def form_valid(self,form):
		print '--------------------------'
		#To allow for a customer to subscribe
		stripe.api_key = settings.STRIPE_SECRET_KEY
		# Creating a customer with customer description and the stripe token we passed from the form(donate.html).
		customer_data = {
			'description': 'donation',
			'card': form.cleaned_data['stripe_token']
		}
		#We passed in the dictionary from above and use ** to unpack the dictionary as kwargs
		customer = stripe.Customer.create(**customer_data)
		# I created a subscriptions on the dashboard and named it donation and set it to an amount of $5 as defacto.
		customer.subscriptions.create(plan="donation")
		#finish off the form valid, so we return to the page thank_you
		#
		return super(DonateView, self).form_valid(form)


# Create your views here.


