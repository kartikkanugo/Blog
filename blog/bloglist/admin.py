from django.contrib import admin

# Register your models here.
from .models import Stories


class StoriesAdmin(admin.ModelAdmin):
    list_display = ("story_id", "story_title", "story_author", "pub_date")


admin.site.register(Stories, StoriesAdmin)
