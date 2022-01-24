from django.shortcuts import render
from django.views.generic import TemplateView


class BlogView(TemplateView):
    template_name = "campaign/blog.html"


class DonarView(TemplateView):
    template_name = "campaign/donar.html"


class EquipoView(TemplateView):
    template_name = "campaign/equipo.html"