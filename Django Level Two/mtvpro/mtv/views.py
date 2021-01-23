from django.shortcuts import render
from django.http import HttpResponse
from mtv.models import Users
# Create your views here.

def index(request):
    my_dict = {"insert_me":"Go to the users information"}
    return render(request,"mtv/index.html",context=my_dict)


def usersss(request):
    usr_list = Users.objects.order_by('first_name')
    usr_dict = {"abcd":usr_list}
    return render(request,"mtv/enduser.html",context=usr_dict)
