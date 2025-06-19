from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
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

# def searchView(request):
#     query = request.GET.get('search_text')

#     result_products = Turf.objects.filter(name__icontains = query)
#     context =  {
#         'turfs' : result_turfs,
#         'query' : query,
#         'search_bar' : True
#     }

#     template = loader.get_template('search_results.html')
#     return HttpResponse(template.render(context, request))


