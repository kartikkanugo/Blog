from django.shortcuts import render
from bloglist.models import Stories

# Create your views here.
def index(request):
    story = Stories.objects.all()

    return render(
        request, "homepage/index.html", {"Stories": [30, 20, 10], "stor": story}
    )