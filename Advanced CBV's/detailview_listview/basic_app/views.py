from django.shortcuts import render
from django.views.generic import View,TemplateView,DetailView,ListView
from basic_app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    # ListView automatically generates the context_object_name of the model followed by '_list' in this case the model name is School so 'school_list'
    # We can also define our own context_object_name as:
    # context_object_name = 'schools'

    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
