# Generated by Django 4.0.5 on 2022-06-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0008_alter_post_thumbnail_response_to_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
