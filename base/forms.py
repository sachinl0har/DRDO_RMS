from django.forms import DateTimeInput, ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, BookUser

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'bio']

class BookUserForm(ModelForm):
    class Meta:
        model = BookUser
        fields = ['title', 'bookStartTime', 'bookEndTime']
        widgets = {
            'bookStartTime': DateTimeInput(attrs={'type': 'datetime-local'}),
            'bookEndTime': DateTimeInput(attrs={'type': 'datetime-local'}),
        }