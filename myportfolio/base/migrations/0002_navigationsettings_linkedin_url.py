# Generated by Django 5.0.2 on 2024-02-24 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigationsettings',
            name='linkedin_url',
            field=models.URLField(blank=True, verbose_name='LinkedIn URL'),
        ),
    ]
