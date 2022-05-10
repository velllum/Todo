from django.urls import path, include

from .routers import router

urlpatterns = [
    path('', include('api.urls.auth')),
    path('', include(router.urls)),
]