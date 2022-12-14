from django.contrib import admin

# Register your models here.
from .models import Stories, StoryLinks


class StoryLinksAdmin(admin.ModelAdmin):
    list_display = ("link_id", "story_key_func", "link", "link_type", "link_name")


class StoriesAdmin(admin.ModelAdmin):
    list_display = ("story_id", "story_title", "story_author", "pub_date")


admin.site.register(StoryLinks, StoryLinksAdmin)
admin.site.register(Stories, StoriesAdmin)
