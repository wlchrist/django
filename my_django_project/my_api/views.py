from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def my_api_view(request):
    return JsonResponse({'message': 'Hello from Django!'})