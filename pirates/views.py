from django.shortcuts import render
from django.views.generic import TemplateView

class ListaTesourosView(TemplateView):
    template_name = "lista_tesouros.html"
