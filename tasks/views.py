from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskCreateForm, TaskUpdateForm
from tasks.models import SimpleTask

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = SimpleTask
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10
    form_class = TaskCreateForm
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by('completed', '-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

def toggle_complete(request, pk):
    task = SimpleTask.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return HttpResponse("Task status updated.")

@login_required
def task_update(request, pk):
    task = SimpleTask.objects.get(pk=pk)
    form = TaskUpdateForm(request.POST or None, instance=task)
    if request.method == 'POST':
        task.user = request.user
        if form.is_valid():
            task = form.save()
            return redirect('task-list')
    return render(request, 'partials/task_detail_form.html', {"form": form, "task": task, 
                                                       "task_update_url": reverse('task-update', args=[pk])})
    
@login_required
def task_delete(request, pk):
    task = SimpleTask.objects.get(pk=pk)
    task.delete()
    return redirect('task-list')
    
@login_required
def task_create(request):
    form = TaskCreateForm(request.POST or None)
    if request.method == 'POST':
        task = form.save(commit=False)
        task.user = request.user
        if form.is_valid():
            task.save()
            return redirect('task-list')
    return render(request, 'partials/task_detail_form.html', {"form": form, "task_create_url": reverse('task-create')})