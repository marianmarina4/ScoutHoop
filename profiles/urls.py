from django.urls import path
from .views import ProfileListView, ProfileDetailView
from players.views import PlayerDetailView

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='profile_list'),
    path('<username>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('player/<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
])