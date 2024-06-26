# Generated by Django 5.0.4 on 2024-04-22 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name', models.CharField(max_length=99, verbose_name='Название страницы')),
                ('slug', models.SlugField(max_length=15, verbose_name='Фрагмент url-адреса')),
                ('url', models.CharField(max_length=199, verbose_name='Полный url-адрес')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
