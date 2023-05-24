from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login, name = 'user_login'),
    path('logout_view/', views.logout_view, name = 'logout_view'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('user_profile', views.user_profile, name = 'user_profile'),
]