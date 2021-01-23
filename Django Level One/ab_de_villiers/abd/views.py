from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def abcd(request):
    abdlist = {"insert_me":"Also called as Mr. 360"}
    return render(request,"abd/mr360.html",context=abdlist)
