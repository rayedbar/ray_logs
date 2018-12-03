"""Define urls for logs"""

from django.urls import path, include

from . import views

app_name = 'logs'
urlpatterns = [
    path('', views.home, name='home'),
]

