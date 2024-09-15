from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.auth_view(), name='login'),
    path('logout/', auth_views.LogoutView.auth_view(), name='logout'),
    path('register/', auth_views.register.as_view(), name='register'),
    path('profile/', auth_views.profile.as_view(), name='profile'),
]