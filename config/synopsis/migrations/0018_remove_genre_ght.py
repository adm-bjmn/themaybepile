# Generated by Django 4.1.3 on 2023-03-23 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synopsis', '0017_remove_genre_genre_human_text_genre_ght'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='ght',
        ),
    ]