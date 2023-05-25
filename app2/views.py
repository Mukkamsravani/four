from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string2(request):
    return HttpResponse('this is app2 string')
def app2(request):
    return render(request,'app2.html')
