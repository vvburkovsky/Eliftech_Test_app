from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('delete_item/<int:id>/', views.delete_item, name='delete_item'),
    path('delete_items_all/', views.delete_items_all, name='delete_items_all'),


]