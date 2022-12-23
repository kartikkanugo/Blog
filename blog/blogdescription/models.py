from django.db import models
import os
from bloglist.models import Stories


def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s.%s" % (instance.story_key.story_id, instance.object_name, ext)
    return os.path.join("images", filename)


class StoryLinks(models.Model):
    class LinkTypes(models.IntegerChoices):
        IMAGE = 1
        VIDEO = 2

    link_id = models.BigAutoField(primary_key=True)
    story_key = models.ForeignKey(Stories, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=200)
    link_type = models.IntegerField(choices=LinkTypes.choices, default=LinkTypes.IMAGE)
    url_link = models.URLField(max_length=200, blank=True)
    image_file = models.ImageField(upload_to=content_file_name, blank=True)

    def story_key_func(self):
        return f"{self.story_key.story_id}"

    def __str__(self):
        return f"{self.object_name} of type {self.link_type} connected to story {self.story_key}"