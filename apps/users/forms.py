from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(
        attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'address',
                'placeholder': 'Электронная почта'
            }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password1',
                'placeholder': 'Введите пароль'
            }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(
        attrs={
                'class': 'form-control',
                'type': 'password',
                'name': 'password1',
                'placeholder': 'Повторите пароль'
            }))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'fname',
                'placeholder': 'Имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'lname',
                'placeholder': 'Фамилия'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'name': 'username',
                'placeholder': 'Логин'
            }),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'username',
            'name': 'username',
            'placeholder': 'Логин'
        }
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'type': 'password',
            'name': 'password',
            'placeholder': 'Введите пароль'
        }
    ))