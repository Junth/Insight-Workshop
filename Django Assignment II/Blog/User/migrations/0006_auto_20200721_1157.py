# Generated by Django 3.0.8 on 2020-07-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_user_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(blank=True, default='default-img.png', null=True, upload_to=''),
        ),
    ]
