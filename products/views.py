#products/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Product

# Create your views here.
class HomePageView(TemplateView):
    template_name ='home.html'