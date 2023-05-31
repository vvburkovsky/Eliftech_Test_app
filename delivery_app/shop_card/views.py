from django.shortcuts import redirect, render
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

def delete_item (request, id):
    item = Basket.objects.get(id=id)
    item.delete()

    return redirect(basket)

def delete_items_all (request):
    Basket.objects.all().delete()

    return redirect('/')