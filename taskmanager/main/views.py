from urllib import request
from django.shortcuts import render, redirect
from .models import Task
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'tasks' : tasks})

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

class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    seccess_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.save()
        return redirect('Home')  # Redirect to the Home view after successful registration

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))