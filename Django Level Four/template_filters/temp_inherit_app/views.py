from django.shortcuts import render

# Create your views here.


def index(request):
    context_dict = {"text":"Hello World!","number":1000}
    return render(request,"temp_inherit_app/index.html",context_dict)


def relativeurl(request):
    return render(request,"temp_inherit_app/relative_url_templates.html")


def other(request):
    return render(request,"temp_inherit_app/other.html")