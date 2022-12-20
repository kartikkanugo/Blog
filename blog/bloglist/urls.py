from django.urls import include, path
from . import views


app_name = "bloglist"
urlpatterns = [
    # path("", views.index, name="blog_list"),
    path("", views.IndexListView.as_view(), name="blog_list")
]
