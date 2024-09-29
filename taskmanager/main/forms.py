from .models import Task
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class TaskForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('В работе', 'В работе'),
        ('Сделано', 'Сделано'),
    ]
    
    PRIORITY_CHOICES = [
        ('Высокий', 'Высокий'),
        ('Средний', 'Средний'),
        ('Низкий', 'Низкий'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Task
        fields = ["title", "task", "status", "priority", "deadlines"]
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            "task": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            "deadlines": forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Выберите дату и время', 'type': 'datetime-local'}),
        }

    def save(self, commit=True, user=None):  
        task = super().save(commit=False)
        if user:  
            task.user = user
        if commit:
            task.save()
        return task

class LoginForm(AuthenticationForm):
    """Форма входа на сайт по имени пользователя и паролю."""

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)  
        self.fields['username'].widget.attrs['autofocus'] = True