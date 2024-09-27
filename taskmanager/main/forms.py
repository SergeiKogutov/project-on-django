from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "status", "priority", "deadlines"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите статус'
            }),
            "priority": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите приоритет'
            }),
            "deadlines": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дедлайн, формат:дата "дд.мм.гг" время "сс.мм.чч"'
            }),
        }