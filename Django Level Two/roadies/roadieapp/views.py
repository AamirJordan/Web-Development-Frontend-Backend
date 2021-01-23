from django.shortcuts import render
from django.http import HttpResponse
from roadieapp.models import Roadies

# Create your views here.

def index(request):
    vicdic = {"insert_me":"All gang members"}
    return render(request,"roadieapp/index.html",context=vicdic)



def vault(request):
    road_list = Roadies.objects.order_by("first_name")
    road_dict = {"prince":road_list}
    return render(request,"roadieapp/vault.html",context=road_dict)
