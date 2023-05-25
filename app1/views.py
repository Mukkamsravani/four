from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def string(request):
    return HttpResponse('this is app1 string response')
def app1(request):
    return render(request,'app1.html')