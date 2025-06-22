from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name =  'homepage'),
    path('about', views.aboutView, name =  'aboutpage'),
    path('contact', views.contactView, name =  'contactpage'),
    path('turf/add', views.AddTurf.as_view(), name ='add_turf'),
    path('turf/<int:pk>',views.TurfDetails.as_view(), name = 'turf_detail'),
    path('turfs/search', views.searchView, name = 'search'),
    
]