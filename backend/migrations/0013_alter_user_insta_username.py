# Generated by Django 4.0.4 on 2022-05-27 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0012_alter_post_userr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_insta',
            name='username',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]