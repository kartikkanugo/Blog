# Generated by Django 4.1.4 on 2022-12-23 07:14

import blogdescription.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("bloglist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="StoryLinks",
            fields=[
                ("link_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("object_name", models.CharField(max_length=200)),
                (
                    "link_type",
                    models.IntegerField(
                        choices=[(1, "Image"), (2, "Video")], default=1
                    ),
                ),
                ("url_link", models.URLField(blank=True)),
                (
                    "image_file",
                    models.ImageField(
                        blank=True, upload_to=blogdescription.models.content_file_name
                    ),
                ),
                (
                    "story_key",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bloglist.stories",
                    ),
                ),
            ],
        ),
    ]
