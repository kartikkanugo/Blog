from django.db import models



class Subscriber(models.Model):
    email_id = models.BigAutoField(primary_key=True)
    email = models.EmailField()

    def __str__(self):
        return self.email
