"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from marketing.views import HomePage
from subscribers.views import subscriber_new
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import AccountList
from accounts.views import account_cru

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home"),
    path('signup/',subscriber_new, name='sub_new'),
    path('account/list/', AccountList.as_view(), name='account_list'),
    path('login/', LoginView.as_view(template_name="login.html"), name="user_login"),
    path('logout/', LogoutView.as_view(), name='home'),
    path('account/<int:uuid>/', include('accounts.urls')),
    path('account/new/', account_cru, name='account_new'),
]
