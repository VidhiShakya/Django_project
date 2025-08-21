from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1 style= color:red;>Hello, world!</h1>")


def home(request):
    return render(request=request, template_name='index.html')