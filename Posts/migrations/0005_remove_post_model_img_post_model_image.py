# Generated by Django 4.1.7 on 2023-04-04 05:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_remove_post_model_image_post_model_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='img',
        ),
        migrations.AddField(
            model_name='post_model',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]
