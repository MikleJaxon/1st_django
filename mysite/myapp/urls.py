from django.urls import path
from myapp.views import index,userinfo,indexItem,add_item, update_item

app_name = "myapp"

urlpatterns = [
    path('', index),
    
    path('<int:prod_id>/', indexItem, name = "detail"),
    
    path('userinfo/', userinfo),
    
    path('additem/', add_item, name= "add_item"),
    
    path('updateitem/<int:prod_id>/', update_item, name= "update_item"),
    

    
    
]
