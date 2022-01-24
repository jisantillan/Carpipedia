from .views import *
from django.urls import path, include

urlpatterns = [
    path('',
         BlogView.as_view(),
         name='blog'),
    path('contribuye/',
         DonarView.as_view(),
         name='contribuye'),
    path('equipo/',
         EquipoView.as_view(),
         name='equipo'),
]
