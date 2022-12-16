
from django.urls import include, path
from . import views


app_name = "bloglist"
urlpatterns = [
    path("", views.index, name="blog_list"),
]
