#products/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product
from .forms import ProductForm

# Create your views here.
class HomePageView(TemplateView):
     template_name ='home.html'

def home(request):
    if request.method == "POST":
        filled_form = ProductForm(reqquest.POST)
        if filled_form.is_valide():
            note = "Thank you for visiting this page!Lowest price %s  in your zipcode %s  
            will return below" %(filled_form.cleaned_data['item1'], 
            filled_form.cleaned_data['item2'],) 
            new_form = ProductForm()
            return render(request, 'home.html', {'productform':form})             
        else:   
             form = ProductForm()
             return render(request, 'home.html', {'productform':form})