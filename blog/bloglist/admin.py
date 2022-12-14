from django.contrib import admin

# Register your models here.
from .models import Stories, StoryLinks

admin.site.register(Stories)
admin.site.register(StoryLinks)