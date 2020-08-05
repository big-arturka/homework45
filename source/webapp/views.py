from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from django.http import HttpResponseNotAllowed
from webapp.forms import TaskForm
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = Task.objects.all()

        context['tasks'] = task
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context


class TaskCreateView(View):
    def get(self, request):
        return render(request, 'task_create.html',
                      context={'form': TaskForm()})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})


class TaskUpdateView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(initial={'title': task.title,
                                 'description': task.description,
                                 'status': task.status,
                                 'type': task.type})
        return render(request, 'task_update.html', context={'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.status = form.cleaned_data['status']
            task.description = form.cleaned_data['description']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_update.html',
                          context={'form': form,
                                   'task': task})


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_delete.html', context={'task': task})

    def post(self, request):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')