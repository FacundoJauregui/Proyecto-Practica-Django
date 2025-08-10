from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def myfirst_view(request):
    data = {
        'message': 'Hello, this is my first view in Django!'
    }
    return JsonResponse(data)
