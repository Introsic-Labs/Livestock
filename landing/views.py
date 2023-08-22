from django.shortcuts import render
from django.views.defaults import page_not_found

# Create your views here.

def home(request):
    return render(request, "landing/home.html")

def handler404(request, exception):
    return render(request, 'error/404.html', status=404)
