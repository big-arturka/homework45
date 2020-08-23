from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Task, Project
from webapp.forms import TaskForm
from django.views.generic import View, FormView, DetailView, CreateView, UpdateView


class TaskView(DetailView):
    template_name = 'task/task_view.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
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
        return redirect('project_view', pk=project.pk)


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task/task_update.html'
    fields = ['title', 'description', 'project', 'status', 'task_type']

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.kwargs.get('pk'),
                                            'project_pk': self.kwargs.get('project_pk')})

# class TaskUpdateView(FormView):
#     template_name = 'task/task_update.html'
#     form_class = TaskForm
#
#     def dispatch(self, request, *args, **kwargs):
#         self.task = self.get_object(Task)
#         self.project = self.get_object(Project)
#         return super().dispatch(request, *args, **kwargs)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = self.task
#         return context
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs.pop('initial')
#         kwargs['instance'] = self.task
#         return kwargs
#
#     def form_valid(self, form):
#         self.task = form.save()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('task_view', kwargs={'pk': self.task.pk})
#
#     def get_object(self, model):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(model, pk=pk)


class TaskDeleteView(View):
    def get(self, request, project_pk, pk):
        task = get_object_or_404(Task, pk=pk)
        project = get_object_or_404(Project, pk=project_pk)
        return render(request, 'task/task_delete.html', context={'task': task,
                                                                 'project': project})

    def post(self, request, project_pk, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('project_view', pk=project_pk)
