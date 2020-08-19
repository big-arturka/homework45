from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Task
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import View, TemplateView, FormView, ListView


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    paginate_by = 2
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Task.objects.all()

        if not self.request.GET:
            data = Task.objects.all()

        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(title__icontains=search) | Q(author__icontains=search))

        return data


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=pk)
        context['task'] = task
        return context


class TaskCreateView(FormView):
    template_name = 'task_create.html'
    form_class = TaskForm

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})


class TaskUpdateView(FormView):
    template_name = 'task_update.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('initial')
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)


class TaskDeleteView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'task_delete.html', context={'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('index')
