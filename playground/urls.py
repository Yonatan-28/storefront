from django.urls import path
from . import views

# no playground/hello/ because we've already called it on the main urls python
urlpatterns = [
    path("hello/", views.say_hello)
]