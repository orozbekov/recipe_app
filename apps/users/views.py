from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView
from requests import request
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .models import CustomUser
from .serializers import CustomUserSerializer

from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm, LoginForm


def all_in_one(request):
    return render(request, 'sign-up.html', {
        'login_form': LoginForm(),
        'register_form': RegisterUserForm()
    })


class RegisterUser(View):

    template_name = 'sign-up.html'

    def get(self, request):
        context = {
            'form': RegisterUserForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):

        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        context = {
            'user_form': user_form
        }
        return render(request, self.template_name, context)


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'sign-up.html', {'form_user': form, 'error': error})




def log_out(request):
    logout(request)
    return redirect(reverse('home'))


class CustomUserListAPIView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Get a list of users",
        responses={'200': CustomUserSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


