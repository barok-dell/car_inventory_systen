from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('', views.index, name='home'),  # Map '/' to the index view, with a name
]