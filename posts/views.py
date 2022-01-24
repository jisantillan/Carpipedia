from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import Post, Categoria
from users import views
from django.contrib.auth.mixins import UserPassesTestMixin


class IsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().propietario


class PostDetailView(DetailView):
    template = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentario_form"] = ComentarioForm
        return context

    def get_success_url(self):
        return '/'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        form.instance.slug = slugify(form.instance.titulo)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    queryset = Post.objects.order_by("-fecha_creacion")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['top_posts_semanal'] = Post.objects.annotate(
            num_likes=Count('likes')
        ).filter(
            fecha_creacion__gte=timezone.now() - timezone.timedelta(days=7)
        ).order_by('-num_likes', '-fecha_creacion')[:10]
        context['top_posts_comentados'] = Post.objects.annotate(
            num_comments=Count('comentarios')
        ).filter(
            fecha_creacion__gte=timezone.now() - timezone.timedelta(days=7)
        ).order_by('-num_comments', '-fecha_creacion')[:10]
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('categorias'):
            queryset = queryset.filter(
                categorias=self.request.GET.get('categorias')
            )
        return queryset


class PostDeleteView(IsOwnerMixin, DeleteView):
    model = Post
    success_url = "/"


class CommentDeleteView(DeleteView):
    model = Comentario

    def get_success_url(self):
        return reverse_lazy("post-detail",
                            kwargs={'slug': self.object.post.slug})


class PostUpdateView(IsOwnerMixin, SuccessMessageMixin, UpdateView):
    model = Post
    success_message = 'El post se actualizó correctamente!'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'slug': self.object.slug})


def comentar_post(request):
    """ Allows to comment a post """
    post = get_object_or_404(Post, slug=request.POST.get('slug'))
    comentario = request.POST.get('cuerpo')
    form = ComentarioForm
    if comentario:
        comentario = Comentario.objects.create(
            post=post,
            user=request.user,
            cuerpo=comentario,
        )
    context = {
        'comentario_form': form,
        'comentarios': post.comentarios.all(),
        'post': post,
        'comentario': comentario,
    }
    if request.is_ajax():
        html = render_to_string('posts/comentarios_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})


def responder_comentario(request):
    """ Allows to respond to a comment """
    comentario = get_object_or_404(Comentario,
                                   pk=request.POST.get('pk_comentario'))
    respuesta = request.POST.get('respuesta')
    if respuesta:
        respuesta = Comentario.objects.create(
            post=comentario.post,
            user=request.user,
            cuerpo=respuesta,
            comentario_padre=comentario,
        )
    context = {
        'comentario_form': ComentarioForm,
        'respuestas': comentario.comentarios_hijos.all(),
        'post': comentario.post,
        'comentarios': comentario.post.comentarios.all(),
    }
    if request.is_ajax():
        html = render_to_string('posts/comentarios_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})


def like_post(request):
    post = get_object_or_404(Post, slug=request.POST.get('slug'))
    is_liked = False
    is_disliked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        is_disliked = False
    else:
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
            is_disliked = False
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'is_disliked': is_disliked,
    }
    if request.is_ajax():
        html = render_to_string('posts/like_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})


def dislike_post(request):
    post = get_object_or_404(Post, slug=request.POST.get('slug'))
    is_disliked = False
    is_liked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        is_disliked = False
        is_liked = False
    else:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked = False
        post.dislikes.add(request.user)
        is_disliked = True
    context = {
        'post': post,
        'is_disliked': is_disliked,
        'is_liked': is_liked,
    }
    if request.is_ajax():
        html = render_to_string('posts/like_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})