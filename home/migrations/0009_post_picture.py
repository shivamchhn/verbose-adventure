# Generated by Django 2.0.6 on 2018-06-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180626_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, height_field='200', null=True, upload_to='profile_image', width_field='400'),
        ),
    ]