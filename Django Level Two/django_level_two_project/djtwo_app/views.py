from django.shortcuts import render
from django.http import HttpResponse
from djtwo_app.models import User

# Create your views here.

def index(request):
    temp_list = {"insert_me":"Go to/users to see the list of user information"}
    return render(request,"djtwo_app/index.html",context=temp_list)



def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'djtwo_app/users.html',context=user_dict)
