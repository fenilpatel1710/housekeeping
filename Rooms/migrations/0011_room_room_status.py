# Generated by Django 3.0.5 on 2020-04-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rooms', '0010_auto_20200427_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.CharField(choices=[('clean', 'clean'), ('Dirty', 'Dirty'), ('Block', 'Block')], default='Dirty', max_length=50),
        ),
    ]