# Generated by Django 4.0 on 2022-05-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
