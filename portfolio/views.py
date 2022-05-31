from django.http import HttpResponse


def home(request):
    return HttpResponse("This is our Home page")

def about(request):
    data = "some data"
    return HttpResponse(data)

def contact(request):
    return HttpResponse("Contact page")
