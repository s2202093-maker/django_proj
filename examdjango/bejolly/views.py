from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to BeJolly")

def storage(request):
    return HttpResponse("This would be the storage page")
