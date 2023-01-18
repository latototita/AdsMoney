# Generated by Django 4.0 on 2023-01-18 14:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_websitelinks_websitelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('des', models.TextField(max_length=1000000)),
                ('button', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('des', models.TextField(max_length=1000000)),
                ('button', models.CharField(max_length=1000)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('des', models.TextField(max_length=1000000)),
                ('button', models.CharField(max_length=1000)),
            ],
        ),
    ]