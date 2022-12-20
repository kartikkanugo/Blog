from django.shortcuts import render
from django.http import Http404
from bloglist.models import Stories, StoryLinks

# Create your views here.


def blog_description(request, story_id: int):
    try:
        story = Stories.objects.get(pk=story_id)
        story_links = StoryLinks.objects.filter(story_key=story_id).values()
    except Stories.DoesNotExist:
        raise Http404("Story does not exist")
    return render(
        request,
        "blogdescription/index.html",
        {"story": story, "story_links": story_links},
    )
