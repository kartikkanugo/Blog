
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "blogdesc"
urlpatterns = [
    # path("<int:story_id>", views.blog_description, name="blog_description"),
    path("<int:story_id>", views.BlogDescDetailView.as_view(), name="blog_description"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
