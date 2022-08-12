from django.test import TestCase

from apps.recipe.models import Category

class CategoryTest(TestCase):

    def test_category_create(self):
        category = Category.objects.create(title='Бургеры', slug='burgery')
        self.assertEqual(category.title, 'Бургеры')
        self.assertEqual(category.slug, 'burgery')

        with self.assertRaises(ValueError):
            pass

