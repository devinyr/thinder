from django import forms

#simple stripe form with a stripe token we receive from stripe 
#and that is all that wil be used to communicate with stripe(the js code in our donate.html) and our app!

class StripeForm(forms.Form):
    stripe_token = forms.CharField()
    print '++++++++++++++++++'

#we receive the token from the js file in the view