from django.utils import timezone
from ckeditor.fields import RichTextField
from django.db import models

URL = 'https://035d-212-42-120-155.in.ngrok.io'

class Category(models.Model):
    """
    Модель для категории.
    """
    title = models.CharField("Категория", max_length=200, unique=True)
    image = models.ImageField("Изображение", upload_to='categories/')
    description = models.TextField("Описание", blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        return URL + self.image.url

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """
    Модель для еды.
    """
    category = models.ForeignKey(Category, verbose_name="Категория", related_name="recipes", on_delete=models.CASCADE)
    name = models.CharField("Название", max_length=250)
    image = models.ImageField("Изображение", upload_to='recipes/')
    description = models.TextField("Описание", blank=True)
    instructions = RichTextField("Пошаговая инструкция")
    area = models.CharField("Город", max_length=100)
    prep = models.PositiveIntegerField("Подготовка", max_length=20, help_text="Укажите время в минутах")
    cook = models.PositiveIntegerField("Приготовление", max_length=20, help_text="Укажите время в минутах")
    slug = models.SlugField(max_length=200, unique=True)
    youtube_url = models.URLField("Сыылка на YouTube", max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def category_name(self):
        return self.category.title
    
    @property
    def image_url(self):
        return URL + self.image.url

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(to=Recipe, related_name='recipes', on_delete=models.CASCADE)
    ingredient = models.CharField("Ингредиент", max_length=150)

    def __str__(self):
        return self.recipe.name



class RecipeStatistic(models.Model):
    """
    Модель для статистики.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    date = models.DateField('Дата', default=timezone.now())
    views = models.PositiveIntegerField('Просмотры', default=0)

    @property
    def recipe_name(self):
        return self.recipe.name

    def __str__(self):
        return self.recipe.name
