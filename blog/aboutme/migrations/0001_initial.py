# Generated by Django 4.1.4 on 2022-12-27 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutMeDB",
            fields=[
                ("about_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("data", models.TextField()),
            ],
        ),
    ]
