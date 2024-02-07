from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


from .models import Product

# Create your views here.
# def index(request):
#     items = Product.objects.all()
#     context = {
#         'items':items
#     }
#     return render(request, "myapp/index.html", context)


class ProductListView(ListView):
    model = Product
    template_name = "myapp/index.html"
    context_object_name = "items"


class detailListView(DetailView):
    model = Product
    template_name = "myapp/detail.html"
    context_object_name = "item"

# def indexItem(request, prod_id):
#     item = Product.objects.get(id = prod_id)
#     context = {
#         'item':item
#     }
#     return render(request, "myapp/detail.html", context=context)

@login_required
def add_item(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        
        description = request.POST.get("description")
        image = request.FILES["upload"]
        seller = request.user
        item = Product(name=name, price=price, description=description, image=image, seller=seller)
        item.save()
    return render(request, "myapp/additem.html")

@login_required
def update_item(request, prod_id):
    item = Product.objects.get(id = prod_id)
    if request.method == "POST":
        item.name = request.POST.get("name")
        item.price = request.POST.get("price")
        item.description = request.POST.get("description")
        item.image = request.FILES.get("upload", item.image)
        item.save()
        return redirect("/myapp/")
    context = {
        'item':item
    }
    
    return render(request, "myapp/updateitem.html", context)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("myapp:index")    

# def delete_item(request, prod_id):
#     item = Product.objects.get(id = prod_id)
#     if request.method == "POST":
#         item.delete()
#         return redirect("/myapp/")
#     context = {
#         'item':item
#     }
#     return render(request, "myapp/deleteitem.html", context)


