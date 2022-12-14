# Generated by Django 4.1 on 2022-08-12 10:39

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Категория')),
                ('image', models.ImageField(upload_to='categories/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('image', models.ImageField(upload_to='recipes/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('instructions', ckeditor.fields.RichTextField(verbose_name='Пошаговая инструкция')),
                ('area', models.CharField(max_length=100, verbose_name='Город')),
                ('prep', models.PositiveIntegerField(help_text='Укажите время в минутах', max_length=20, verbose_name='Подготовка')),
                ('cook', models.PositiveIntegerField(help_text='Укажите время в минутах', max_length=20, verbose_name='Приготовление')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('youtube_url', models.URLField(blank=True, max_length=250, verbose_name='Сыылка на YouTube')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipe.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime(2022, 8, 12, 10, 39, 20, 105110, tzinfo=datetime.timezone.utc), verbose_name='Дата')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=150, verbose_name='Ингредиент')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipe.recipe')),
            ],
        ),
    ]
