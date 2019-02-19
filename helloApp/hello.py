import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.management import execute_from_command_line

#configure required django settings
settings.configure(
	DEBUG=True,
	SECRET_KEY='thisisab@dkeybut1tw1lld0',
	ROOT_URLCONF=sys.modules[__name__],
	)

#configure the view
def index(request):
	return HttpResponse('Hello, world')

#configure the url
urlpatterns = [
    path('hello', index),
]

#to exexute it from the command line
if __name__ == "__main__":
	execute_from_command_line(sys.argv)


#run this by python hello.py runserver