from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'forms_app/home.html')

def contatti(request):
    return render(request,'forms_app/contatto.html')