from django.shortcuts import render
from demo import forms

# Create your views here.


def index(request):
    return render(request,"demo/index.html")


def taurus(request):
    alpha = forms.zodiac()

    if request.method == "POST":
        form = forms.zodiac(request.POST)

        if form.is_valid():
            print("Name: " + form.cleaned_data["name"])
            print("Email: " + form.cleaned_data["email"])



    return render(request,"demo/completeform.html",{"form":alpha})
