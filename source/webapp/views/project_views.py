from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import ProjectForm
from webapp.models import Task, Project
from django.views.generic import ListView, DetailView, CreateView


class IndexView(ListView):
    template_name = 'project/index.html'
    context_object_name = 'projects'
    paginate_by = 3
    paginate_orphans = 2

    def get_queryset(self):
        return Project.objects.all()


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project


# class ProjectCreateView(CreateView):
#     template_name = 'project/project_create.html'
#     form_class = ProjectForm
#     model = Project
#
#     def get_success_url(self):
#         return reverse('project_view', kwargs={'pk': self.object.pk})


