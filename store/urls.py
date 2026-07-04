from django.urls import path
from .views import (
    CharacterListView,
    CharacterDetailView,
    WalletView,
    ClaimCharacterView
)

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='character-list'),
    path('characters/<int:pk>/', CharacterDetailView.as_view(), name='character-detail'),
    path('wallet/', WalletView.as_view(), name='wallet'),
    path('characters/<int:pk>/claim/', ClaimCharacterView.as_view(), name='claim-character'),
]