# Generated by Django 4.0.5 on 2022-06-13 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0009_alter_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
