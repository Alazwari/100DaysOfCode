from django.shortcuts import render, redirect
from . import models
from . import forms


def index(request):
    form = forms.TaskForm(request.POST)
    if form.is_valid():
        Instance = form.save(commit=False)
        Instance.save()
        return redirect('/')
    context = {
        'tasks' : models.Task.objects.all(),
        'form' : form
    }
    return render(request, 'index.html', context)


# def add_task(request):
#     context = {}
#     return redirect('/')