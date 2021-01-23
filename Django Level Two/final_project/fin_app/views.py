from django.shortcuts import render
from django.http import HttpResponse
from fin_app.models import Enduser

# Create your views here.


def index(request):
    index_dict = {"insert_me":"You just got me"}
    return render(request,"fin_app/index.html",context=index_dict)



def ender(request):
    end_list = Enduser.objects.order_by("first_name")
    end_dict = {"roadies":end_list}
    return render(request,"fin_app/eu.html",context=end_dict)
