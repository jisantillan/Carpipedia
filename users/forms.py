from django import forms
from .models import User, Avatar
from datetime import date


class DateInput(forms.DateInput):
    model = User
    """ Sirve para mostrar el date picker en el template """
    input_type = 'date'


class AvatarInput(forms.Select):
    template_name = "widgets/select_avatar.html"
    option_template_name = "widgets/select_avatar_option.html"

    def __init__(self, *args, **kwargs):
        self.user = None
        super().__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["opciones"] = Avatar.objects.filter(nivel__lte=self.user.nivel)
        return context


class UserForm(forms.ModelForm):
    """ Formulario de edición de datos de usuario """
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['avatar'].widget.user = user

    def clean(self):
        if self.cleaned_data['fecha_de_nacimiento']:
            if self.cleaned_data['fecha_de_nacimiento'] > date.today():
                self.add_error(
                    'fecha_de_nacimiento',
                    "* La fecha de nacimiento no puede ser futura"
                )
                raise forms.ValidationError(
                    "- Existen errores en el formulario:\
                    La fecha de nacimiento no puede ser futura."
                )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'pais',
            'fecha_de_nacimiento',
            'biografia',
            'intereses',
            'avatar',
            'email']
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(
                attrs={'placeholder': 'dd/mm/aaaa', 'max': '2022-01-01'}
            ),
            'avatar': AvatarInput(),
        }