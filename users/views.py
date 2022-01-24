from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from .models import User
from posts.models import Post
from .forms import UserForm

# Create your views here.

# class deleteAccountMDL(UpdateView):
#    template_name = "accounts/login.html"


class UsrDetailView(DetailView):
    template = 'usr_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            propietario=self.get_object()).order_by('-fecha_creacion')
        return context


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    success_message = 'El perfil se actualizó correctamente!'
    form_class = UserForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return f'/accounts/detalle/{self.get_object().pk}'


class UserDeleteView(DeleteView):
    model = User()
    success_url = "/"

    def get_object(self, queryset=None):
        return self.request.user


class IsOwnerMixin(object):
    permission_denied_message = ("No sos el dueño de este perfil,"
                                 " no podés editarlo")

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != request.user:
            raise PermissionDenied(self.get_permission_denied_message())
        return super().dispatch(request, *args, **kwargs)

    def get_permission_denied_message(self):
        """
        Override this method to override the
        permission_denied_message attribute.
        """
        return self.permission_denied_message


def get_premium_access(request):
    """ View que sirve para cambiar el nivel de premium """
    user = request.user
    if user.is_authenticated:
        nivel = request.POST.get('nivel')
        user.nivel = nivel
        user.save()
        return redirect('/accounts/editar/')
    else:
        return redirect('/accounts/login')
