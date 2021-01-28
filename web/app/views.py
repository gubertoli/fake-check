from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from .ml import preprocess

class FakeText(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(attrs={"style": "resize: none"}), label='')

# Create your views here.
def index(request):
    if request.method == "POST":
        form = FakeText(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text_input"]
            resultado = preprocess.process_text(text)
            return render(request, "app/index.html", {
                "form" : FakeText(),
                "zero" : "{:.2%}".format(resultado.flat[0]),
                "um" : "{:.2%}".format(resultado.flat[1])
            })
        else:
            return HttpResponseRedirect(reverse("app:index"))
    
    return render(request, "app/index.html", {
        "form" : FakeText()
    })
