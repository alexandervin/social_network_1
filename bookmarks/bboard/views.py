from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from .models import import Bb


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    model = Bb