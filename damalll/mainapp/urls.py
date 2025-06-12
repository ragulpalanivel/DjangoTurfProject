from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name =  'homepage'),
    path('turf/add', views.AddTurf.as_view(), name ='add_turf'),
]