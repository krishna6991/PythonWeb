from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Subscriber(models.Model):
	user_rec = models.ForeignKey(User, on_delete=models.CASCADE)
	address_one = models.CharField(max_length=100)
	address_two = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	stripe_id=models.CharField(max_length=30,blank=True)

	class Meta:
		verbose_name_plural = 'subscribers'

		def __unicode__(self):
			return u"%s 's Subscription Info" % self.user_rec

	def charge(self, request, email,fee):
		stripe.api_key = settings.STRIPE_SECRET_KEY

		#get the credit card detail submitted by the form.
		token= request.POST['stripeToken']
		#create a customer
		stripe_customer = stripe.Customer.create(
			card=token,
			description=email
			)

		#save the stripe ID to the customer's profile.
		self.stripe_id = stripe_customer.id
		self.save()

		#charge the customer instead of card.
		stripe.Charge.create(
			amount=fee,
			currency="inr",
			customer=stripe_customer.id
			)

		return stripe_customer
