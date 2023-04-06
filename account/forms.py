from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(max_length=70, label="User Name",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'user name'}))
    password = forms.CharField(max_length=70, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder':'password', 
                                                                 'aria-label':'Password', 
                                                                 'aria-describedby':'password-addon'}))

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs = {'class': "form-control", 
                                                                                      'placeholder': "password", 
                                                                                      'aria-label':"password", 
                                                                                      'aria-describedby':"password-addon"}))
    
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs = {'class': "form-control",
                                                                                                   'placeholder': "password confirmation",
                                                                                                   'aria-label':"password",
                                                                                                   'aria-describedby':"password-addon"}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'phone','profil_photo', 'password1', 'password2']
        widgets = {
            'username' :forms.TextInput(attrs = {'class': "form-control", 
                                                 'placeholder': "username", 
                                                 'aria-label':"Username", 
                                                 'aria-describedby':"username-addon"}),
            
            'email':forms.EmailInput(attrs = {'class': "form-control", 
                                              'placeholder': "email",
                                              'aria-label':"email",
                                              'aria-describedby':"email-addon"}),
            
            'first_name' :forms.TextInput(attrs = {'class': "form-control",  
                                                   'placeholder': "first name", 
                                                   'aria-label':"first name", 
                                                   'aria-describedby':"name-addon"}),
            
            'last_name' :forms.TextInput(attrs = {'class': "form-control",  
                                                  'placeholder': "last name", 
                                                  'aria-label':"last name", 
                                                  'aria-describedby':"name-addon"}),
            
        
        }