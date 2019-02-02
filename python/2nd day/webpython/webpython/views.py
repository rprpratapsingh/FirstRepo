
from django.http import HttpResponse

def home(request):
    obj = HttpResponse("<h1>Home Page</h1><hr>")
    return obj

def about(request):
    obj = HttpResponse("<h1>About Page</h1><hr>")
    return obj