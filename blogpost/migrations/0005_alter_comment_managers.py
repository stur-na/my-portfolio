# Generated by Django 4.0.5 on 2022-06-13 12:03

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0004_post_content_post_overview_post_title'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='comment',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
