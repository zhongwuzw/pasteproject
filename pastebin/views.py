from django.shortcuts import render
from django.views.generic.list import ListView
from pastebin.models import Paste
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class HomeView(ListView):
    model = Paste
    template_name = 'paste_list.html'
    context_object_name = 'object_list'
    
class DetailItemView(DetailView):
    model = Paste
    template_name = 'paste_detail.html'
    context_object_name = 'object' 
    
class AddFormView(CreateView):
    model = Paste
    template_name = 'paste_form.html'
    context_object_name = 'form'
    
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(AddFormView, self).dispatch(request,*args,**kwargs)
    
    