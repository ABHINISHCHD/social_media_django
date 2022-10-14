from dataclasses import field
from statistics import mode
from tkinter import Widget
from turtle import textinput
from xml.dom.minidom import Attr
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages


class registration(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


    class Meta:
        
        model=User
        fields=['username','email','password1','password2']
        widgets ={
            'username': forms.TextInput(attrs={
                'placeholder':'name',
                'class':"form-control",
                'style':'margin:10px auto'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder':'email',
                'class':"form-control",
                'style':'margin:10px auto'
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder':'password',
                'class':"form-control",
                'style':'margin:10px auto'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder':'confirm password',
                'class':"form-control",
                'style':'margin:10px auto'
            })
        }


class profile_create(forms.ModelForm):
    class Meta:
        model=profile
        fields=['bio','dp','location']
        widgets={
            'bio':forms.TextInput(
                attrs={
                    'placeholder':'bio',
                    'class':"form-control",
                                        
                }
            ),
            'location':forms.TextInput(
                attrs={
                    'placeholder':'location',
                    'class':"form-control",
                    
                }
            ),
        }

class posting_post(forms.ModelForm):
    caption=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",'placeholder':"write caption",'style':'margin-bottom:10px;'}))
    class Meta:
        model=posting
        fields=['post','caption']
        



class user_update(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control"}))
    class Meta:
        model=User
        fields=['username','email']

class profile_update(forms.ModelForm):
    bio=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    location=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    class Meta:
        model=profile
        fields=['bio','dp','location']

class login_form(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control"}))

class comment(forms.ModelForm):
    comment=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=comment
        fields=['comment']