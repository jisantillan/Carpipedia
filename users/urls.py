from .views import *
from django.urls import path, include
from .views import UserUpdateView

urlpatterns = [
    path('detalle/<int:pk>/', UsrDetailView.as_view(), name='usr-detail'),
    path('editar/', UserUpdateView.as_view(), name='user_update'),
    path('eliminar/', UserDeleteView.as_view(), name='user-delete'),
    path('hacerse-premium/', get_premium_access, name='get-premium-access'),
]