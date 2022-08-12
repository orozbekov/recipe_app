from django.contrib.auth import get_user_model
from django.test import TestCase

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email='tima@gmail.com', password='qwerty', username='tima', 
            first_name='Tima', last_name='Orozbekov'
            )
        self.assertEqual(user.email, 'tima@gmail.com')
        self.assertEqual(user.username, 'tima')
        self.assertEqual(user.first_name, 'Tima')
        self.assertEqual(user.last_name, 'Orozbekov')
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            email='orozbekov@gmail.com', password='qwerty', username='orozbekov', 
            first_name='Tima', last_name='Orozbekov'
        )
        self.assertEqual(admin_user.email, 'orozbekov@gmail.com')
        self.assertEqual(admin_user.username, 'orozbekov')
        self.assertEqual(admin_user.first_name, 'Tima')
        self.assertEqual(admin_user.last_name, 'Orozbekov')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)


        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)