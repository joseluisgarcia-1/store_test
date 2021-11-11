from django.urls import path, re_path, include
from catalogo.apps.home.views import about_index, contacto_view

urlpatterns = [
    path('about/', about_index),
    path('contacto/', contacto_view)
]