# Generated by Django 3.2.8 on 2021-10-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gulmohar',
            name='image_src',
            field=models.CharField(default='hello', max_length=200),
        ),
    ]
