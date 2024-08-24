from django.db.models.base import Model as Model
from .forms import UserRegisterForm, ProfileForm, EmailForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django import forms
from .models import Profile

# Create your views here.

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    
    # Chequeamos que el form sea válido
    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        Profile.objects.create(user=self.object)
        return response
    
    # Si se registra con exito redirigimos
    def get_success_url(self):
        return reverse_lazy('home') + '?register'
    
    
    def get_form(self, form_class=None):
       form = super(RegisterView, self).get_form()
       
       # Modificamos en tiempo real
       form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
       form.fields['first_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
       form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
       form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
       form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
       form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repite la contraseña'})
       return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'
    
    def get_object(self):
        #Recuperar el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    
        
@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'
    
    def get_success_url(self):
        return reverse_lazy('profile_email')+ '?update'
    
    def get_object(self):
        #Recuperar el objeto que se va a editar
        return self.request.user
    
    def get_form(self, form_class=None):
         form = super(EmailUpdate, self).get_form()
         form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
         
         return form