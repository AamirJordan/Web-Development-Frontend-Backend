from django.conf.urls import url
from template_app import views

urlpatterns = [
    #url(r'',views.index),
    url(r'',views.helpindex)        # The function called first will affect the page
]
