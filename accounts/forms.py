from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder':'Username...', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder':'Email...', 'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'placeholder':'Password...', 'class': 'form-control'})        
        self.fields['password2'].widget.attrs.update({'placeholder':'Repeat password...', 'class': 'form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
