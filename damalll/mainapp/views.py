from django.shortcuts import render
from .models import Turf
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# def homeView(request):
#     template_name = 'home.html'
#     turfs = Turf.objects.all() 
#     context = {
#         'turf_list' : turfs

#     }
#     return render(request, template_name, context)

def aboutView(request):
    template_name = 'about.html'
    context ={}
    return render(request, template_name, context)

def contactView(request):
    template_name = 'contact.html'
    context ={}
    return render(request, template_name, context)

class HomeView(ListView):
    template_name = 'home.html'
    model = Turf
    context_object_name = 'turfs'

class AddTurf(CreateView):
    template_name = 'add_turf.html'
    model = Turf
    fields ='__all__'
    success_url = '/'

class TurfDetails(DetailView):
    template_name = 'turf_detail.html'
    model = Turf
    context_object_name = 'turf'
    success_url = '/'


