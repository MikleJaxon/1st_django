from django.urls import path
from myapp.views import index,userinfo,indexItem

app_name = "myapp"

urlpatterns = [
    path('', index),
    
    path('<int:prod_id>/', indexItem, name = "detail"),
    
    path('userinfo/', userinfo),
    

    
    
]
