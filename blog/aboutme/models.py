from django.db import models

# Create your models here.


class AboutMeDB(models.Model):
    about_id = models.BigAutoField(primary_key=True)
    data = models.TextField()