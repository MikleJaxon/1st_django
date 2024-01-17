from django.urls import path
from myapp.views import index,indexItem,add_item, update_item, delete_item

app_name = "myapp"

urlpatterns = [
    path('', index, name = 'index'),
    
    path('<int:prod_id>/', indexItem, name = "detail"),

    
    path('additem/', add_item, name= "add_item"),
    
    path('updateitem/<int:prod_id>/', update_item, name= "update_item"),
    
    path('deleteitem/<int:prod_id>/', delete_item, name= "delete_item"),
    

    
    
]
