from django.urls import path

from . import views

app_name = "subscribermail"
urlpatterns = [
    path("", views.index, name="subscriber_mail"),
]