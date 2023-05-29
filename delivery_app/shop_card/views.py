from django.shortcuts import render
from shop.models import Basket

# Create your views here.
def shop_card (request):
    
    return render(request, 'shop_card\index.html')


def basket (request):

    basket = Basket.objects.all()
    context = {
        'basket': basket
    }

    return render(request, 'shop_card\index.html', context)