
from django.views.generic.base import TemplateView
from .models import AboutMeDB


# Create your views here.
class AboutMeDetailView(TemplateView):
    template_name = "aboutme/index.html"
    model = AboutMeDB

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context