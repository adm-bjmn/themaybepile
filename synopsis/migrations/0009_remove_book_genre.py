# Generated by Django 4.1.3 on 2023-03-23 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('synopsis', '0008_book_seen_by_alter_book_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]