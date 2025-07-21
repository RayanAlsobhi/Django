from django.shortcuts import render
from django.http import HttpResponse
# i try to statr debuging but not work and i just import "debugpy" and it work 
# import debugpy
# debugpy.listen(("localhost", 5678))
# debugpy.wait_for_client()

def calculate():
    x  = 1
    y = 2 
    return x
def say_hello(request):
    x = calculate()
    y = 2
    z = x + y
    return render(request , 'hello.html',{'name':'Rayan'})
