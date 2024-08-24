from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    #Verifica que el email no este registrado
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, pruebe con otro")
        return email
    

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya está registrado, pruebe con otro")
        return email

class ProfileForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ['avatar', 'age','phone_number','bio', 'link']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type':'number','placeholder': 'Número de teléfono'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción personal'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Enlace'}),
        }
        
