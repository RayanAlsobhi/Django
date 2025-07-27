from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist 
from django.db.models import Q,F
from store.models import Product,OrderItem
# i try to statr debuging but not work and i just import "debugpy" and it work 
# import debugpy
# debugpy.listen(("localhost", 5678))
# debugpy.wait_for_client()


def say_hello(request):
    
    queryset = OrderItem.objects.values('product_id').distinct()
    
    
    return render(request , 'hello.html',{'name':'Rayan','queryset':list(queryset)})


