# Generated by Django 4.2.7 on 2023-12-03 09:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0008_alter_confession_subject_alter_confession_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='confession',
            name='dislikes_users',
            field=models.ManyToManyField(related_name='disliked_confessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='confession',
            name='likes_users',
            field=models.ManyToManyField(related_name='liked_confessions', to=settings.AUTH_USER_MODEL),
        ),
    ]
