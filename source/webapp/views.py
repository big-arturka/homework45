from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseNotAllowed
from webapp.forms import TaskForm


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', context={
        'task': task})


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html',
                      context={'form': TaskForm()})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={'title': task.title,
                                 'description': task.description,
                                 'status': task.status,
                                 'completion_date': task.completion_date})
        return render(request, 'task_update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data['title']
            task.status = form.cleaned_data['status']
            task.description = form.cleaned_data['description']
            task.completion_date = form.cleaned_data['completion_date']
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'task_update.html',
                          context={'form': form,
                                   'task': task})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')


def bulk_delete_view(request):
    Task.objects.filter(id__in=request.POST.getlist('item')).delete()
    data = Task.objects.all()
    return redirect('index')

