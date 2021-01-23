from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wrestler(request):
    return HttpResponse("Its me Roman")

def finisher(request):
    big_dog = {"insert_me":"Believe That!"}
    return render(request,"roman_reigns/roman.html",context=big_dog)
