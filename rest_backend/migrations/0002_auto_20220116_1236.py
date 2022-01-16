# Generated by Django 3.2.10 on 2022-01-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directmessage',
            name='baudrate',
            field=models.PositiveSmallIntegerField(choices=[(1, 512), (2, 1200), (3, 2400)], default=2, verbose_name='Скорость передачи'),
        ),
        migrations.AddField(
            model_name='transmitter',
            name='baudrate',
            field=models.PositiveSmallIntegerField(choices=[(1, 512), (2, 1200), (3, 2400)], default=2, verbose_name='Скорость передачи'),
        ),
    ]
