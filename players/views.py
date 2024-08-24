from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Player
from .forms import PlayerForm

@method_decorator(login_required, name='dispatch')
class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'
    
    # def get_form(self, form_class=None):
    #    form = super(PlayerCreateView, self).get_form()
       
    #    form.fields ['first_name'].widget = forms.TextInput(attrs={'class': 'form-control'}),
    #    form.fields['last_name'].widget = forms.TextInput(attrs={'class': 'form-control'}),
    #    form.fields['height'].widget = forms.NumberInput(attrs={'class': 'form-control'}),
    #    form.fields['weight'].widget = forms.NumberInput(attrs={'class': 'form-control'}),
    #    form.fields['position'].widget = forms.Select(attrs={'class': 'form-control'}),
    #    form.fields['last_teams'].widget = forms.Textarea(attrs={'class': 'form-control'}),
    #    form.fields['current_team'].widget = forms.TextInput(attrs={'class': 'form-control'}),
    #    form.fields['status'].widget = forms.Select(attrs={'class': 'form-control'}),
    #    return form

    def form_valid(self, form):
        form.instance.agent = self.request.user.profile  # Asigna el jugador al agente conectado
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile')  # Redirige al perfil del agente después de agregar un jugador

@method_decorator(login_required, name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'

    def get_success_url(self):
        return reverse_lazy('profile')
