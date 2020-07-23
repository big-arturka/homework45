from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES


def index_view(request):
    data = Task.objects.all()
    return render(request, 'index.html', context={
        'tasks': data
    })


def task_create_view(request):
    if request.method == 'GET':
        return render(request, 'task_create.html',
                      context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        if request.POST.get('completion_date') == '':
            task = Task.objects.create(title=title, status=status)
        else:
            completion_date = request.POST.get('completion_date')
            task = Task.objects.create(title=title, status=status,
                                       completion_date=completion_date)
        context = {'task': task}
        return render(request, 'task_view.html', context)