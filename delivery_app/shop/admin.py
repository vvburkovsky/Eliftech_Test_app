from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Restorans)
admin.site.register(Restorans_menu)

class BasketAdmin(admin.ModelAdmin):
    list_display = ['order_name', 'img', 'price']
admin.site.register(Basket, BasketAdmin)