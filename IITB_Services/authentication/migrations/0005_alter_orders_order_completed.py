# Generated by Django 3.2.8 on 2021-10-25 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Order_completed',
            field=models.BooleanField(default=False),
        ),
    ]
