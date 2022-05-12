from django.urls import path

from . import views


# Локально-нормативные акты
urlpatterns = [
    path('', views.ListView.as_view(), name='list'),
    path('detail/', views.DetailView.as_view(), name='detail'),
    path('create/', views.CreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]