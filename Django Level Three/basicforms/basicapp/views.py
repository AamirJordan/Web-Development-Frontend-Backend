from django.shortcuts import render
from basicapp import forms

# Create your views here.


def index(request):
    return render(request,"basicapp/index.html")


def form_name_view(request):
    hallo = forms.SignUpForm()



    if request.method == "POST":
        form = forms.SignUpForm(request.POST)



        if form.is_valid():
            #Do Something
            print("Validation SUCCESS")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])




    return render(request,"basicapp/form_page.html",{"form":hallo})
