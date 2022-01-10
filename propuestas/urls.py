from django.urls import path
from .views import index, ClienteListView

urlpatterns = [
    path('', index, name="index"),
    path('clientes/', ClienteListView.as_view(), name="listado_clientes"),
]