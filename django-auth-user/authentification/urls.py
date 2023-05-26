from .api import RegisterApi
from django.conf.urls import url
from django.urls import path, include


urlpatterns = [
      path('', RegisterApi.as_view()),
]