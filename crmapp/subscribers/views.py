from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import SubscriberForm

def subscriber_new(request):
	if request.method == 'POST':
		form = SubscriberForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.form.cleaned_data['email']

			user = User(username=username, email=email)
			user.set_password(password)
			user.save()
			s_query = form.cleaned_data['search_query']
			s_results= SomeTable.objects.filter(name=s_query)
			return HttpResponseRedirect('/success/')
	else: 
		form = SubscriberForm()

	return render(request, 'subscribers/subscriber_new.html', {'form':form,})
