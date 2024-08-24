from django.urls import path
from .views import RegisterView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),
]