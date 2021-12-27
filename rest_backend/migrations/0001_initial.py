# Generated by Django 3.2.10 on 2021-12-27 03:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DirectMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capcode', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)], verbose_name='Капкод')),
                ('freq', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(60000000), django.core.validators.MaxValueValidator(999999999)], verbose_name='Частота (Гц)')),
                ('fbit', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], verbose_name='Источник')),
                ('codepage', models.PositiveSmallIntegerField(choices=[(1, 'lat'), (2, 'cyr'), (3, 'linguist')], verbose_name='Кодировка текста')),
                ('message', models.TextField(max_length=950, verbose_name='Сообщение')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NewsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'уведомления'), (2, 'новости'), (3, 'погода'), (4, 'курсы валют'), (5, 'юмор'), (6, 'гороскоп'), (7, 'резерв'), (8, 'резерв 2')], verbose_name='Тип рассылки')),
                ('message', models.TextField(max_length=950, verbose_name='Новостное сообщение')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_number', models.PositiveIntegerField(unique=True, verbose_name='Абонентский номер')),
                ('capcode', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)], verbose_name='Приватный капкод')),
                ('fbit', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], verbose_name='Источник')),
                ('codepage', models.PositiveSmallIntegerField(choices=[(1, 'lat'), (2, 'cyr'), (3, 'linguist')], verbose_name='Кодировка текста')),
            ],
        ),
        migrations.CreateModel(
            name='Transmitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('freq', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(60000000), django.core.validators.MaxValueValidator(999999999)], verbose_name='Частота (Гц)')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=950, verbose_name='Сообщение')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_sent', models.BooleanField(default=False)),
                ('pager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_backend.pager', verbose_name='Пейджер-получатель')),
            ],
        ),
        migrations.AddField(
            model_name='pager',
            name='transmitter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_backend.transmitter', verbose_name='Трансмиттер'),
        ),
        migrations.CreateModel(
            name='NewsChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.PositiveSmallIntegerField(choices=[(1, 'уведомления'), (2, 'новости'), (3, 'погода'), (4, 'курсы валют'), (5, 'юмор'), (6, 'гороскоп'), (7, 'резерв'), (8, 'резерв 2')], verbose_name='Тип рассылки')),
                ('capcode', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999999)], verbose_name='Новостной капкод')),
                ('fbit', models.PositiveSmallIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], verbose_name='Источник')),
                ('codepage', models.PositiveSmallIntegerField(choices=[(1, 'lat'), (2, 'cyr'), (3, 'linguist')], verbose_name='Кодировка текста')),
                ('transmitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_backend.transmitter', verbose_name='Трансмиттер')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО клиента')),
                ('datar', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('pagers', models.ManyToManyField(to='rest_backend.Pager', verbose_name='Пейджеры клиента')),
            ],
        ),
    ]
