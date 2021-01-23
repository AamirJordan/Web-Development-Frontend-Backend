from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.


#   FUNCTION BASED VIEW --------------------------------------------------------
#   def index(request):
#        my_dict = {"injectme":"Hii this is because of Function Based View"}
#       return render(request,'index.html',context=my_dict)


#   CLASS BASED VIEW -----------------------------------------------------------
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'This has been injected in the content'
        return context
