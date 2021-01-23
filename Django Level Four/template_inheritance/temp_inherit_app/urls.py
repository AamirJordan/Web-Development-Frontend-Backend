from django.conf.urls import url
from temp_inherit_app import views

app_name = 'calltempinh'

urlpatterns = [
    url(r'gotorelative/',views.relativeurl,name='relativity'),
    url(r'gotoother/',views.other,name='unanimous')
]
