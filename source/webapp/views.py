from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


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
                      context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        description = request.POST.get('description')
        completion_date = request.POST.get('completion_date')
        task = Task.objects.create(title=title, status=status,
                                   completion_date=completion_date, description=description)
        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html',
                      context={'task': task})
    elif request.method == 'POST':
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.description = request.POST.get('description')
        task.completion_date = request.POST.get('completion_date')
        task.save()
        return redirect('task_view', pk=task.pk)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])