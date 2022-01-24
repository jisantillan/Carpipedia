from django import forms
from django.forms.models import ModelMultipleChoiceField
from tinymce.widgets import TinyMCE
from .models import Post, Categoria, Comentario


class PostForm(forms.ModelForm):
    categorias = ModelMultipleChoiceField(queryset=Categoria.objects.all())
    titulo = forms.CharField()

    class Meta:
        model = Post
        fields = ('categorias', 'titulo', 'contenido')


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('cuerpo', )
        widgets = {'cuerpo': forms.TextInput(
            attrs={
                'class': 'form-control',
                'value': '',
                'placeholder': 'Escribe un comentario...'}
        )}