# Generated by Django 4.1.3 on 2023-02-16 16:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('synopsis', '0006_remove_book_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
