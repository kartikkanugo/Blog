from django.contrib import admin
from .models import StoryLinks


class StoryLinksAdmin(admin.ModelAdmin):
    list_display = (
        "link_id",
        "story_key_func",
        "object_name",
        "link_type",
        "url_link",
    )


admin.site.register(StoryLinks, StoryLinksAdmin)