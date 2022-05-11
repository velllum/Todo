from django.urls import path

from . import views


# Локально-нормативные акты
urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('detail/', views.NoteDetailView.as_view(), name='detail'),
    path('create/', views.NoteCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.NoteEditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.NoteDeleteView.as_view(), name='delete'),
]