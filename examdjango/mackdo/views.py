from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Welcome to Mackdo")

def storage(request):
    return HttpResponse("Form page will be here")
