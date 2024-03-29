# Generated by Django 4.0.4 on 2022-05-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_commentpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='timestamps',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user_insta',
            name='followers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_insta',
            name='following',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user_insta',
            name='post_num',
            field=models.IntegerField(default=0),
        ),
    ]
