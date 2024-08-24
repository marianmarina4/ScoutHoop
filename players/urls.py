from django.urls import path
from .views import PlayerCreateView, PlayerUpdateView

urlpatterns = [
    path('add/', PlayerCreateView.as_view(), name='player_add'),
    path('edit/<int:pk>/', PlayerUpdateView.as_view(), name='player_edit'),
]
