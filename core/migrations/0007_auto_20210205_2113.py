# Generated by Django 3.1.1 on 2021-02-05 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210205_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='tweet_images/'),
        ),
    ]