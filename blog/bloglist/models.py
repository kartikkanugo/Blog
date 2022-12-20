from django.db import models
import os


def content_file_name(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s_%s.%s" % (instance.story_key.story_id, instance.object_name, ext)
    return os.path.join("photos", filename)


# Create your models here.
class Stories(models.Model):
    class Authors(models.TextChoices):
        SONU = "Sushma Kanugo"
        MISC = "Unknown"

    class Ratings(models.IntegerChoices):
        LOW = 0
        NORMAL = 1
        HIGH = 2

    story_id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField("Date Published")
    story_title = models.CharField(max_length=200)
    story = models.TextField()
    story_gist = models.CharField(max_length=600)
    story_author = models.CharField(
        max_length=100, choices=Authors.choices, default=Authors.SONU.value
    )
    chapter_id = models.IntegerField(
        default=-1,
        help_text="Put chapter ID 1 if the story will have chapters else leave it as it is",
    )
    story_chapter_link_id = models.IntegerField(
        default=-1, help_text="Id of the story to which the Chapter is linked?"
    )
    rating = models.IntegerField(default=Ratings.NORMAL, choices=Ratings.choices)

    def __str__(self):
        return f"{self.story_id} Title {self.story_title[:30]}"


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
