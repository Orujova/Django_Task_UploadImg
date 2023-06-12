from django.shortcuts import render
from .models import *

# Create your views here.

def product_list_view(request):
  product = Product.objects.all()

  context = {
    "product":product,
  }
  
  return render(request, "index.html",context)
