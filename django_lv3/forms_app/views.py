from django.shortcuts import render
from django.http import HttpResponse     
from .forms import FormContatto
# Create your views here.

def homepage(request):
    return render(request,'forms_app/home.html')

# def contatti(request):
#     form=FormContatto()
#     context={"form": form}
#     return render(request,'forms_app/contatto.html',context)

def contatti(request):
    if request.method=="POST":
        form=FormContatto(request.POST)
        if form.is_valid():
            print("il form è valido")
            print("NOME:",form.cleaned_data["nome"])
            print("COGNOME:",form.cleaned_data["cognome"])
            print("MAIL:",form.cleaned_data["email"])
            print("CONTENUTO:",form.cleaned_data["contenuto"])

            return HttpResponse("<h1>Grazie per averci contattato</h1>")
    else:
        form=FormContatto()

    context={"form": form}
    return render(request,'forms_app/contatto.html',context)