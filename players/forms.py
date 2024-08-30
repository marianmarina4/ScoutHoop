from django import forms
from .models import Player,Team

class PlayerForm(forms.ModelForm):
     
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'avatar','birthday', 'height', 'weight', 'position', 'status']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'birthday' : forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
    
class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'country', 'year_played']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'year_played': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
        