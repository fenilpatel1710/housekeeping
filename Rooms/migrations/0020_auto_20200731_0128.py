# Generated by Django 3.0.5 on 2020-07-31 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0019_auto_20200731_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deepclean',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
