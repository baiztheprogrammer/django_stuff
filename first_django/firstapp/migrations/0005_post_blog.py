# Generated by Django 3.1.3 on 2020-11-26 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstapp.blog'),
        ),
    ]