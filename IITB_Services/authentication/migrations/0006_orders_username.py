# Generated by Django 3.2.8 on 2021-10-25 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_orders_order_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='username',
            field=models.CharField(default='hello', max_length=30),
        ),
    ]