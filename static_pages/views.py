from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'static_pages/home.html')

def contact(request):
    return HttpResponse('<h1>Contact page. Under construction</h1>')
