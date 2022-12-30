from django.shortcuts import render
from bloglist.models import Stories
from .forms import SubscriberForm

# Create your views here.
def index(request):
    story = Stories.objects.all()

    form = SubscriberForm(request.POST or None)

    if form.is_valid():

        form.save()

    return render(request, "homepage/index.html", {"form": form, "stor": story})