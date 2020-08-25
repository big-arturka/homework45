from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

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


class TaskCreateView(CreateView):
    template_name = 'task/task_create.html'
    form_class = TaskForm
    model = Task

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('project_view', pk=project.pk)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    form_class = TaskForm

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


class TaskDeleteView(DeleteView):
    template_name = 'task/task_delete.html'
    model = Task
    success_url = reverse_lazy('index')
