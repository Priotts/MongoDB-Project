from django.urls import path
from . import views

urlpatterns = [
    path('order_view/', views.order_view, name = 'order_view'),
    path('order/', views.order, name = 'order')
]