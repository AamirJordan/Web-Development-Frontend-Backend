from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


#   FUNCTION BASED VIEW --------------------------------------------------------
#   def index(request):
#        return render(request,'index.html')

                #----------------   OR  ------------------

#   def index(request):
#        return HttpResponse("anything written here won't affect the page")




#   CLASS BASED VIEW -----------------------------------------------------------
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based View")

                #----------------    OR  --------------------

#class CBView(View):
#    def get(self,request):
#        return render(request,'index.html')
