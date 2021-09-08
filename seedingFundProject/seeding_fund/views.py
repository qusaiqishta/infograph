from django.shortcuts import render , HttpResponse


def index(request):
    return HttpResponse('it is working')