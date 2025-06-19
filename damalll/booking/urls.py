from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:turf_id>/', views.book_turf, name='book_turf'),
]
