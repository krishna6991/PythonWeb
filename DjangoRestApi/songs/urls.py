from django.urls import path, include, re_path
from .views import ListSongsView

urlpatterns = [
    path('songs/',ListSongsView.as_view(), name="songs-all"),
]
