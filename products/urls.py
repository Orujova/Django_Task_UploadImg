from django.urls import path
from . import views

app_name="products"

urlpatterns = [
    path('index/',views.product_list_view,name="index"),
   
    
]
