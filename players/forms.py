from django import forms
from .models import Player,Team

class PlayerForm(forms.ModelForm):
     
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'avatar','birthday', 'height', 'weight', 'position', 'status', 'yt_link']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control-update'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control-update'}),
            'avatar' : forms.ClearableFileInput(attrs={'class': 'form-control-update'}),
            'birthday' : forms.DateInput(attrs={'class': 'form-control-update', 'type': 'date'}),
            'height': forms.NumberInput(attrs={'class': 'form-control-update'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control-update'}),
            'position': forms.Select(attrs={'class': 'form-control-update'}),
            'status': forms.Select(attrs={'class': 'form-control-update'}),
            'yt_link': forms.TextInput(attrs={'class': 'form-control-update'})
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
        
        