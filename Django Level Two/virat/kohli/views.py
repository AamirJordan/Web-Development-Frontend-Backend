from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def nickname(request):
    vkdict = {"insert_me":"The Run Machine"}
    return render(request,"kohli/batsman.html",context=vkdict)
