from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, User

# Create your views here.
def index(request):
    items = Product.objects.all()
    context = {
        'items':items
    }
    return render(request, "myapp/index.html", context)


def indexItem(request, prod_id):
    item = Product.objects.get(id = prod_id)
    context = {
        'item':item
    }
    return render(request, "myapp/detail.html", context=context)

def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["upload"]
        item = Product(name=name, price=price, description=description, image=image)
        item.save()
    return render(request, "myapp/additem.html")
    

def userinfo(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request, "myapp/userinfo.html", context)
