from django.shortcuts import render , redirect
from .models import Rewan2
from .forms import RewanForm
from django.http import HttpResponse



def welcome (request):
    return render(request,"welcome.html")


def load_form(request):
    form = RewanForm
    return render(request , "index.html",{'form': form})


def add(request):
    form=RewanForm(request.POST)
    form.save()
    return redirect('/show')


def show(request):
    rewan2=Rewan2.objects.all
    return render(request, 'show.html',{'rewan2': rewan2})



def edit(request,id):
    rewan2 = Rewan2.objects.get(id=id)
    return render(request,'edit.html',{'rewan2':rewan2})

def update(request,id):
    rewan2 = Rewan2.objects.get(id=id)
    form = RewanForm(request.POST,instance=rewan2)
    form.save()
    return redirect('/show')

def delete(request,id):
    rewan2= Rewan2.objects.get(id=id)
    rewan2.delete()
    return redirect('/show')    

