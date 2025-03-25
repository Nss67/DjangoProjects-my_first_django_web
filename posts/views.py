from django.http import HttpResponse

def index(request):
    # body
    return HttpResponse("<h1>Hello, World.</h1>")

def home(request):
    return HttpResponse("<h3>Welcome to my home page...</h3>")

