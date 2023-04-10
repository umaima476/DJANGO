from django.shortcuts import render
from django.http import HttpResponse

def functionName(request):
    return render(request, 'second.html')

# Create your views here.
