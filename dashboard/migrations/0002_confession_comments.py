# Generated by Django 4.2.7 on 2023-12-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='confession',
            name='comments',
            field=models.TextField(blank=True),
        ),
    ]