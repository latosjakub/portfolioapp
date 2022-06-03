from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def about(request):
    data = "some data"
    return HttpResponse(data)

def contact(request):
    return HttpResponse("Contact page")

def list(request):
    return HttpResponse("list page")
