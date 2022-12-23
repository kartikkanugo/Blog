from django.shortcuts import render
from django.http import Http404
from bloglist.models import Stories
from django.views.generic import DetailView
from blogdescription.models import StoryLinks
from django.conf import settings


# Create your views here.


# def blog_description(request, story_id: int):
#    try:
#        story = Stories.objects.get(pk=story_id)
#        story_links = StoryLinks.objects.filter(story_key=story_id).values()
#    except Stories.DoesNotExist:
#        raise Http404("Story does not exist")
#    return render(
#        request,
#        "blogdescription/index.html",
#        {"story": story, "story_links": story_links},
#    )


class BlogDescDetailView(DetailView):
    model = Stories
    template_name = "blogdescription/index.html"
    pk_url_kwarg = "story_id"
    context_object_name = "object"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        for i in StoryLinks.objects.filter(story_key=self.kwargs["story_id"]).values():
            if i["link_type"] == 1:
                context[i["object_name"]] = i["image_file"]
            else:
                context[i["object_name"]] = i["url_link"]

        context["MEDIA_ROOT"] = settings.MEDIA_ROOT
        context["MEDIA_URL"] = settings.MEDIA_URL
        # print(context["stlinks"])
        return context