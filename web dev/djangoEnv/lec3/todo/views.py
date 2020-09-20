from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

class form_add(forms.Form ):
    task = forms.CharField(label="New Task")
    imp = forms.IntegerField(label="Importance")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    if "imp" not in request.session:
        request.session["imp"] = []
    return render(request,"todo/index.html",{
        "tasks":request.session["tasks"],
        "imp":request.session["imp"]
    })
def add(request):
    if request.method=="POST":
        form = form_add(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            impo = form.cleaned_data["imp"]
            request.session["tasks"]+=[task]
            request.session["imp"]+=[impo]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, "todo/add.html",{
            "form": form
        })
    return render(request,"todo/add.html",{
        "form": form_add()

    })
