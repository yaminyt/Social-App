# Generated by Django 4.1.7 on 2023-04-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=100, verbose_name='Name')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='DateTime')),
                ('body', models.CharField(max_length=500, verbose_name='body')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
