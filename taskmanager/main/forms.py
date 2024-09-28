from .models import Task
from django.forms import ModelForm, TextInput, Textarea, CharField, EmailInput, EmailField, PasswordInput
from django.contrib.auth.models import User

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
                'placeholder': 'Введите дедлайн, формат:дата "дд.мм.гг" время "чч.мм.сс"'
            }),
        }



# class RegisterUserForm(UserCreationForm):
#     username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
#     email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-input'}))
#     password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
#     password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')