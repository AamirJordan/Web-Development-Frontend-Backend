from django.shortcuts import render
#from django.http import HttpResponse
#from fin_app.models import Enduser
from fin_app.forms import NewUserForm

# Create your views here.


def index(request):
    index_dict = {"insert_me":"You just got me"}
    return render(request,"fin_app/index.html",context=index_dict)



def ender(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)


        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Error form invalid")

    return render(request,"fin_app/eu.html",{"form":form})
