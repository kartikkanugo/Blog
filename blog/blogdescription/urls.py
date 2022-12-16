
from django.urls import include, path
from . import views


app_name = "blogdesc"
urlpatterns = [
    path("<int:story_id>", views.blog_description, name="blog_description"),
]
