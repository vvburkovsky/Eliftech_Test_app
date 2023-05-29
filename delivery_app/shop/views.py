from django.shortcuts import render, redirect
from .models import Restorans_menu, Basket

# Create your views here.
def shop (request):

    menus = Restorans_menu.objects.all()
    context = {
        'menu': menus
    }

    return render(request, 'shop\index.html', context)

def order (request):
    b = Basket()
    b.order_name = request.POST['description']
    b.img = request.POST['img']
    b.price = request.POST['price']
    b.save()

    return redirect('/')
    #return render(request, 'shop\index.html', context)


def coupons (request):

    menus = Restorans_menu.objects.all()
    context = {
        'menu': menus
    }

    return render(request, 'shop\coupons.html', context)