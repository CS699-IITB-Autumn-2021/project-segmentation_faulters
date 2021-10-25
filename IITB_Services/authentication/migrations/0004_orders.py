# Generated by Django 3.2.8 on 2021-10-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_gulmohar_image_src'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_details', models.CharField(max_length=500)),
                ('Vendor', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Order_completed', models.BooleanField(default=True)),
            ],
        ),
    ]
