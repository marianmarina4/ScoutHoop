from django.urls import path
from .views import PlayerListView, PlayerCreateView, PlayerUpdateView, PlayerDeleteView,PlayerDetailView,TeamCreateView

urlpatterns = [
    path('', PlayerListView.as_view(), name='player_list'),
    path('add/', PlayerCreateView.as_view(), name='player_add'),
    path('edit/<int:pk>/', PlayerUpdateView.as_view(), name='player_edit'),
    path('delete/<int:pk>/', PlayerDeleteView.as_view(), name='player_delete'),
    path('team/', TeamCreateView.as_view(), name='add_team'),
]
