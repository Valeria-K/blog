# Generated by Django 2.1.5 on 2019-12-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_statistics'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
