from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('coupons/', views.coupons, name='coupons'),


]