from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from .models import Player, Team
from .forms import PlayerForm, TeamForm
from django.shortcuts import render


#  Vista de crear jugadores
@method_decorator(login_required, name='dispatch')
class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'
    
    def form_valid(self, form):
        #  Asigna al field agente el perfil del usuario
        form.instance.agent = self.request.user.profile  
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #  Agregamos los equipos al contexto para usarlo fuera
        context['teams'] = Team.objects.all()
        context['players'] = Player.objects.all()  
        return context

    def get_success_url(self):
        return reverse_lazy('profile')


#  Vista de actualizar jugadores
@method_decorator(login_required, name='dispatch')
class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'players/player_form.html'

    def get_success_url(self):
        return reverse_lazy('profile')


#  Vista de eliminar jugadores
@method_decorator(login_required, name='dispatch')
class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('profile')
    template_name = 'players/player_delete.html'
    
    
#  Vista de Lista de jugadores    
class PlayerListView(ListView):
    model = Player
    
    # Filtrar según Field si esta presente en solicitud GET
    def get_queryset(self):
        queryset = super().get_queryset()
        #Si encontramos 
        
        # Filtro por posición
        position = self.request.GET.get('position')
        if position:
            queryset = queryset.filter(position=position)
        
        # Filtro por altura
        height = self.request.GET.get('height')
        if height:
            queryset = queryset.filter(height=height)
        
        
        # Filtro por año
        birthday_year = self.request.GET.get('birthday_year')
        if birthday_year:
            queryset = queryset.filter(birthday__year=birthday_year)
        
        
        # Filtro por Agente
        agent = self.request.GET.get('agent')
        if agent:
            queryset = queryset.filter(agent__user__id=agent)
        
        
        # Filtro por estado
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)    
         
        return queryset
        
       
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = Player._meta.get_field('position').choices
        context['agents'] = User.objects.all()
        context['years'] = Player.objects.values_list('birthday__year', flat=True).distinct().order_by('birthday__year') 
        return context


#  Vista de Equipo
@method_decorator(login_required, name='dispatch')
class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'players/player_form_team.html'

    def get_success_url(self):
        return reverse_lazy('player_add')
    
    