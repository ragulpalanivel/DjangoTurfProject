from django.shortcuts import render
from .models import Turf
from django.views.generic import CreateView, ListView, DetailView

# def home (request):
#     return render(request, 'base.html')


class HomeView(ListView):
    template_name = 'home.html'
    model = Turf
    context_object_name = 'turfs'

class TurfDetails(DetailView):
    template_name = 'home.html'
    model = Turf
    context_object_name = 'turfs'