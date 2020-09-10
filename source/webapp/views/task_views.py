from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Task, Project
from webapp.forms import TaskForm
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        context['project'] = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        return context


class TaskCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'task/task_create.html'
    form_class = TaskForm
    model = Task
    permission_required = 'webapp.add_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm
    permission_required = 'webapp.change_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        return super().has_permission() and self.request.user in project.user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        project = get_object_or_404(Project, pk=self.kwargs.get('project_pk'))
        context['task'] = task
        context['project'] = project
        return context

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.kwargs.get('pk'),
                                            'project_pk': self.kwargs.get('project_pk')})


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    model = Task
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.user.all()

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.project.pk})