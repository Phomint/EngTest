from django.urls import path
from .views import (
    ContatoCreateView,
    ContatoDeleteView,
    ContatoDetailView,
    ContatoListView,
    ContatoUpdateView,
)
app_name = 'contato'
urlpatterns = [
    path('', ContatoListView.as_view(), name='contato-list'),
    path('create/', ContatoCreateView.as_view(), name='contato-create'),
    path('<int:pk>/', ContatoDetailView.as_view(), name='contato-detail'),
    path('<int:id>/update/', ContatoUpdateView.as_view(), name='contato-update'),
    path('<int:id>/delete/', ContatoDeleteView.as_view(), name='contato-delete'),
]
