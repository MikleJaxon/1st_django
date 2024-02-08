from django.urls import path
from myapp.views import index, add_item, update_item, ProductListView, detailListView, ProductDeleteView, PaymentSuccessView, PaymentFailedView, create_checkout_session

app_name = "myapp"

urlpatterns = [
    path('', index, name = 'index'),
    
    # path('', ProductListView.as_view(), name = 'index'),

    # path('<int:prod_id>/', indexItem, name = "detail"),

    path('<int:pk>/', detailListView.as_view(), name = "detail"),

    
    path('additem/', add_item, name= "add_item"),
    
    path('updateitem/<int:prod_id>/', update_item, name= "update_item"),

    path('deleteitem/<int:pk>/', ProductDeleteView.as_view(), name= "delete_item"),

    path('success/', PaymentSuccessView.as_view(), name= "success"),
    path('failed/', PaymentFailedView.as_view(), name= "failed"),
    path('api/checkout-session/<int:id>/', create_checkout_session, name= "api_checkout_session"),
    
    # path('deleteitem/<int:prod_id>/', delete_item, name= "delete_item"),
    

    
    
]
