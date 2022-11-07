from django.http import HttpResponse
from django.shortcuts import render
from .forms import MessaggioModelForm

# Create your views here.


def contact_view(request):
    if request.method=="POST":
        form=MessaggioModelForm(request.POST)
        if form.is_valid():
            nuovo_messaggio=form.save()
            return HttpResponse("<h1>Grazie per averci contattato</h1>")
    else:
        form=MessaggioModelForm()
        context={"form":form}
        return render(request,'prova_pratica/form_contatto.html',context)