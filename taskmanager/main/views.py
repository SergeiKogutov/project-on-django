from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, TaskForm
from django.contrib.auth import authenticate, login

def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)  # Фильтруем задачи по авторизованному пользователю
    else:
        tasks = Task.objects.none()  # Если пользователь не авторизован, показываем пустой QuerySet

    context = {
        'tasks': tasks,
    }
    return render(request, 'main/index.html', context)

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)  # передаём существующую задачу
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = TaskForm(instance=task)

    return render(request, 'main/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)  # Убедитесь, что задача принадлежит авторизованному пользователю
    task.delete()
    return redirect('Home') 

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)  # Передаем авторизованного пользователя
            return redirect('Home')
    else:
        form = TaskForm()
    
    context = {
        'form': form,
    }
    return render(request, 'main/create.html', context)

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    seccess_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        return redirect('Home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

def LoginUser(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('Home')  
            else:
                error = 'Неверное имя пользователя или пароль'
        else:
            error = 'Форма была неверной'

    form = LoginForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/login.html', context)