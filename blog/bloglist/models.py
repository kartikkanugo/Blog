from django.db import models

# Create your models here.
class Stories(models.Model):
    class Authors(models.TextChoices):
        SONU = "Sushma Kanugo"
        MISC = "Unknown"

    story_id = models.BigAutoField(primary_key=True)
    pub_date = models.DateTimeField("Date Published")
    story_title = models.CharField(max_length=200)
    story = models.TextField()
    story_gist = models.CharField(max_length=600)
    story_author = models.CharField(
        max_length=100, choices=Authors.choices, default=Authors.SONU.value
    )

    def __str__(self):
        return f"ID:{self.story_id} with title {self.story_title} was published on {self.pub_date} "


class StoryLinks(models.Model):
    class LinkTypes(models.IntegerChoices):
        IMAGE = 1
        VIDEO = 2

    link_id = models.BigAutoField(primary_key=True)
    story_key = models.ForeignKey(
        Stories, on_delete=models.CASCADE)
    link = models.CharField(max_length=200)
    link_type = models.IntegerField(choices=LinkTypes.choices, default=LinkTypes.IMAGE)
    link_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.link_name} of type {self.link_type} connected to story {self.story_key}"
