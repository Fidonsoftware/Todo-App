from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    works = Work.objects.all()
    form = WorkForm()

    if request.method =="POST":
        form = WorkForm(request.POST)
    if form.is_valid():
          form.save()
    return redirect('/')

    context = {'works':works, 'form': form}
    return render(request, 'work/list.html', context)

def UpdateWork(request,pk):
     works = Work.objects.get(id=pk)

     return render(request, 'work/work_update.html')