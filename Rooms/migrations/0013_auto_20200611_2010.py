# Generated by Django 3.0.5 on 2020-06-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0012_auto_20200508_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('clean', 'clean'), ('dirty', 'dirty'), ('maintenance', 'maintenance')], default='maintenance', max_length=50),
        ),
    ]
