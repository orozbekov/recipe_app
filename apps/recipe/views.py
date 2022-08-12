from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response 
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Sum
from django.utils import timezone
from .models import Category, Recipe, RecipeStatistic, RecipeIngredient
from django.db.models import Q
from .serializers import CategorySerializer, RecipeSerializer, RecipeIngredientSerializer


class RecipeListView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):

        context = {}
        recipe = Recipe.objects.all()[:10]
        category = Category.objects.all()
        popular = RecipeStatistic.objects.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
        ).order_by(
            '-views').all()[:5]
        context['recipe'] = recipe
        context['category'] = category
        context['popular_list'] = popular
        return render(request, template_name=self.template_name, context=context)


class RecipeDetailView(View):
    template_name = 'single-recipe.html'

    def get(self, request, slug, *args, **kwargs):
        context = {}
        recipe = get_object_or_404(Recipe, slug=slug)
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        obj,created = RecipeStatistic.objects.get_or_create(
            defaults={
                'recipe': recipe,
                'date': timezone.now()
            },
            date=timezone.now(), recipe=recipe
        )
        obj.views += 1
        obj.save(update_fields=['views'])
        context['recipe'] = recipe
        context['ingredients'] = ingredients
        return render(request, template_name=self.template_name, context=context)


class RecipesListSearchView(View):

    template_name = 'recipes.html'

    def get(self, request, *args, **kwargs):
        context = {}
        search_query = request.GET.get('search')
        if search_query:
            recipes_list = Recipe.objects.filter(
                Q(name__icontains=search_query) | Q(category__title__icontains=search_query)
            )
        else:
            recipes_list = Recipe.objects.all()
        category = Category.objects.all()
        context['recipes_list'] = recipes_list
        context['categories'] = category
        return render(request, template_name=self.template_name, context=context)



def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def recipes(request):
    return render(request, 'recipes.html')



def tags(request):
    return render(request, 'tags.html')


def tag_template(request):
    return render(request, 'tag-template.html')

def error_404(request):
    return render(request, '404.html')

class CategoryListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Список всех категории.',
        responses={
            '200': CategorySerializer(many=True),
        },
    )

    def get(self, request):
        """
        Список всех категории.
        """
        category = Category.objects.all()
        srz = {'categories': CategorySerializer(category, many=True).data}
        return Response(srz, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Создание категории.',
        request_body=CategorySerializer(many=False),
        responses={
            '201': CategorySerializer(many=False),
        },
    )
    
    def post(self, request):
        """
        Созание категории с заданными данными.
        """
        request_body = request.data
        new_category = Category.objects.create(
            title=request_body['title'],
            description=request_body['description'],
            image=request_body['image']
        )
        srz = CategorySerializer(new_category, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class CategoryDetailAPIView(APIView):

    def get(self, request, category_id):
        """
        fffff
        """
        category = get_object_or_404(Category, id=category_id)
        srz = CategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, category_id, *args, **kwargs):
        """
        Updates the  item with given todo_id if exists
        """
        request_body = request.data

        category = get_object_or_404(Category, id=category_id)
        category.name = request_body['name']
        category.image = request_body['image']
        category.description = request_body['description']
        category.save()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 5. Delete
    def delete(self, request, category_id, *args, **kwargs):
        category_instance = get_object_or_404(Category, id=category_id)
        category_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class RecipeListCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_summary='Список всех блюд.',
        responses={
            '200': CategorySerializer(many=True),
        },
    )
    def get(self, request):
        recipe = Recipe.objects.order_by("?").all()[:1]
        srz = {'meal': RecipeSerializer(recipe, many=True).data}
        return Response(srz, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='Создание еды.',
        request_body=CategorySerializer(many=False),
        responses={
            '201': CategorySerializer(many=False),
        },
    )
    def post(self, request):
        data = {
            'name': request.data['name'],
            'image': request.data['image'],
            'description': request.data['description'],
            'recipe': request.data['recipe'],
            'youtube_url': request.data['youtube_url'],
        }
        serializer = RecipeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EArticleView(View):
#
#     def get(self, request, slug):
#         article = get_object_or_404(Recipe, slug=slug)  # Забираем статью из базы данных
#         context = {}
#
#         # Далее забираем объект сегодняшней статистики или создаём новый, если требуется
#         obj, created = RecipeStatistic.objects.get_or_create(
#             defaults={
#                 "article": article,
#                 "date": timezone.now()
#             },
#             # При этом определяем, забор объекта статистики или его создание
#             # по двум полям: дата и внешний ключ на статью
#             date=timezone.now(), recipe=article
#         )
#         obj.views += 1  # инкрементируем счётчик просмотров и обновляем поле в базе данных
#         obj.save(update_fields=['views'])
#
#         # А теперь забираем список 5 последний самых популярных статей за неделю
#         popular = RecipeStatistic.objects.filter(
#             # отфильтровываем записи за последние 7 дней
#             date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
#         ).values(
#             # Забираем интересующие нас поля, а именно id и заголовок
#             # К сожалению забрать объект по внешнему ключу в данном случае не получится
#             # Только конкретные поля из объекта
#             'recipe_slug', 'recipe__name'
#         ).annotate(
#             # Суммируем записи по просмотрам
#             # Всё суммируется корректно с соответствием по запрашиваемым полям объектов
#             views=Sum('views')
#         ).order_by(
#             # отсортируем записи по убыванию
#             '-views')[:5]  # Заберём последние пять записей
#
#         context['popular_list'] = popular  # Отправим в контекст список статей
#
#         return render(context=context)

# https://evileg.com/ru/post/59/