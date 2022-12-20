from django.shortcuts import render
from django.views.generic.list import ListView
from bloglist.models import Stories

# Create your views here.


def index(request):
    return render(request, "bloglist/index.html")


class IndexListView(ListView):
    model = Stories
    template_name = "bloglist/index.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by("-story_id")
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured"] = self.get_queryset().filter(rating=2).values()[:2]
        return context
