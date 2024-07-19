from django.urls import path
from .views import index, register, user_login, logout_user

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name = 'register_page'),
    path('login/', user_login, name = 'login_page'),
    path('logout/', logout_user, name = 'logout'),
]