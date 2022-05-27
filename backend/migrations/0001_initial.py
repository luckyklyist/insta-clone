# Generated by Django 4.0 on 2022-05-16 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, max_length=100)),
                ('like_count', models.IntegerField()),
                ('pic', models.ImageField(upload_to='insta_pic')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]