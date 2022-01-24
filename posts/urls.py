from .views import *
from django.urls import path, include

urlpatterns = [
    path('detalle/<slug:slug>/',
         PostDetailView.as_view(),
         name='post-detail'),
    path('editar/<slug:slug>/', PostUpdateView.as_view(), name='post-edit'),
    path('crear/', PostCreateView.as_view(), name='post-create'),
    path('', PostListView.as_view(), name='post-list'),
    path('eliminar/<slug:slug>/',
         PostDeleteView.as_view(),
         name='post-delete'),
    path('like/', like_post, name="like_post"),
    path('dislike/', dislike_post, name="dislike_post"),
    path('comentar/', comentar_post, name="comentar_post"),
    path('responder-comentario/',
         responder_comentario,
         name="responder_comentario"),
    path('eliminar-comentario/<int:pk>',
         CommentDeleteView.as_view(),
         name='comment-delete'),
]
