# Generated by Django 4.0.5 on 2022-06-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_info_thumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project_info',
            old_name='thumbnail',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='project_info',
            name='image2',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='project_info',
            name='image3',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
