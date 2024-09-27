from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index1(request):
    return render(request, 'main/index1.html')

def register(request):
    return render(request, 'main/register.html')

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')
        else:
            error = 'форма была неверной' 

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
