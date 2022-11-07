from django import forms

class FormContatto(forms.Form):

    nome=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    cognome=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    contenuto=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Area testuale", "class":"form-control"}))