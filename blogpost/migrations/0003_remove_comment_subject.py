# Generated by Django 4.0.5 on 2022-06-12 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_comment_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='subject',
        ),
    ]
