from django.urls import path
from . import views


urlpatterns = [
    path("", views.help_home, name="help_home"),
]


