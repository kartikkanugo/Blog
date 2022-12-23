from django.db import models


# Create your models here.
class Stories(models.Model):
    class Authors(models.TextChoices):
        SONU = "Sushma Kanugo"
        MISC = "Unknown"

    class Ratings(models.IntegerChoices):
        LOW = 0
        NORMAL = 1
        HIGH = 2

    class Genre(models.TextChoices):
        HORROR = "Horror"
        ROMANCE = "Romance"
        COMEDY = "Comedy"
        DRAMA = "Drama"

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
    genre = models.CharField(
        max_length=100, choices=Genre.choices, default=Genre.DRAMA.value
    )
    story_chapter_link_id = models.IntegerField(
        default=-1, help_text="Id of the story to which the Chapter is linked?"
    )
    rating = models.IntegerField(default=Ratings.NORMAL, choices=Ratings.choices)

    def __str__(self):
        return f"{self.story_id} Title {self.story_title[:30]}"
