# Generated by Django 3.1.3 on 2020-11-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
