from django.urls import path
from myapp.views import add_item, update_item, delete_item, ProductListView, detailListView

app_name = "myapp"

urlpatterns = [
    #path('', index, name = 'index'),
    
    path('', ProductListView.as_view(), name = 'index'),

    #path('<int:prod_id>/', indexItem, name = "detail"),

    path('<int:pk>/', detailListView.as_view(), name = "detail"),

    
    path('additem/', add_item, name= "add_item"),
    
    path('updateitem/<int:prod_id>/', update_item, name= "update_item"),
    
    path('deleteitem/<int:prod_id>/', delete_item, name= "delete_item"),
    

    
    
]
