# Generated by Django 3.2.9 on 2021-11-23 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_backend', '0009_pager'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmitter',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='pager',
            name='id_transmitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_backend.transmitter', verbose_name='Идентификатор трансмиттера'),
        ),
    ]
