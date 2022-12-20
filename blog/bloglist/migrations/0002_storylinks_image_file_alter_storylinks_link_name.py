# Generated by Django 4.1.4 on 2022-12-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloglist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storylinks',
            name='image_file',
            field=models.ImageField(default=1, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storylinks',
            name='link_name',
            field=models.URLField(),
        ),
    ]
