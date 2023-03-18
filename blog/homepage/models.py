from django.db import models

# did something
class Subscriber(models.Model):
    email_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
