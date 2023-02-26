from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime


class HomeView(TemplateView):
    template_name = 'projects/index.html'
    extra_context = {'today': datetime.today()}
