# Generated by Django 4.1.7 on 2023-04-04 05:37

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0005_remove_post_model_img_post_model_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='date_time',
        ),
        migrations.AddField(
            model_name='post_model',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='created DateTime'),
        ),
        migrations.AlterField(
            model_name='post_model',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, verbose_name='image'),
        ),
    ]