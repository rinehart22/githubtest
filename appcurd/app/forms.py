from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth.models import User 
from django.forms import ModelForm 
from .models import Angel

class AngelForm(ModelForm): 
    class Meta: 
        model = Angel 
        fields = '__all__'

class SignupForm(UserCreationForm): 

    class Meta: 
        
        model = User 
        fields = [ 'username', 'email', 'password1', 'password2'] 