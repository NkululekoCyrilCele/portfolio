from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'proj/index.html', {
        'projects': projects
    })


def detail(request, id):
    project_id = get_object_or_404(Project, pk=id)
    return render(request, 'proj/detail.html', {
        'project_id': project_id
    })
