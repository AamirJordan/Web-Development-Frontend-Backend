from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>Demo Test</em")

def helpindex(request):
    helpdict = {'insert_me': "I am here for your help"}
    return render(request,'template_app/help.html',context=helpdict)
