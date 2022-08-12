from django.urls import path

from .views import CustomUserListAPIView, log_out, RegisterUser, log_in, all_in_one

urlpatterns = [
    path('api/v1/user/', CustomUserListAPIView.as_view()),
    path(r'^$', all_in_one, name='all_in_one'),
    path('login/', log_in, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', log_out, name='logout'),
]

