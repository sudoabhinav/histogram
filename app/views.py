from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    """docstring for HomeView"""
    template_name = "app/home.html"
