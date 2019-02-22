from django.urls import path
from .views import account_detail

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
]
