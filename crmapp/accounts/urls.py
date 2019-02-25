from django.urls import path
from .views import account_detail
from account.views import account_cru

urlpatterns = [
    path('', account_detail, name="home"),
    path('edit/', account_cru, name="account_update"),
]
