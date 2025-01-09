from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from tasks.forms import TaskCreateForm, TaskUpdateForm, UserUpdateForm
from tasks.models import SimpleTask

def get_paginated_tasks(request, tasks, tasks_per_page):
    paginator = Paginator(tasks, tasks_per_page)  # Paginate tasks
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return {
        'tasks': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        "task_count": paginator.count,
    }



def index(request):
    return HttpResponse("Hello, world. You're at the index.")

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = SimpleTask
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 5
    form_class = TaskCreateForm
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).order_by('completed', '-updated_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        context['current_page'] = self.request.GET.get('page')
        context.update(get_paginated_tasks(self.request, self.get_queryset(), self.paginate_by))
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request'):  # HTMX request
            return render(self.request, 'partials/task_list_partial.html', context)
        return super().render_to_response(context, **response_kwargs)


@login_required
@require_http_methods(["PATCH"])
def toggle_complete(request, pk):
    task = get_object_or_404(SimpleTask, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    tasks = SimpleTask.objects.filter(user=request.user).order_by('completed', '-updated_at')
    context = get_paginated_tasks(request, tasks, 5)
    return render(request, 'partials/task_list_partial.html', 
                  context)

@login_required
def task_update(request, pk):
    task = get_object_or_404(SimpleTask, pk=pk, user=request.user)
    form = TaskUpdateForm(request.POST or None, instance=task)
    if request.method == 'POST':
        task.user = request.user
        if form.is_valid():
            task = form.save()
            tasks = SimpleTask.objects.filter(user=request.user).order_by('completed', '-updated_at')
            context = get_paginated_tasks(request, tasks, 5)
            return render(request, 'partials/task_list_partial.html', context)
    return render(request, 'partials/task_detail_form.html', {"form": form, "task": task})
                                                       
@login_required
@require_http_methods(["DELETE"])
def task_delete(request, pk):
    task = get_object_or_404(SimpleTask, pk=pk, user=request.user)
    task.delete()
    tasks = SimpleTask.objects.filter(user=request.user).order_by('completed', '-updated_at')
    messages.success(request, 'Task deleted successfully')
    context = get_paginated_tasks(request, tasks, 5)
    return render(request, 'partials/task_list_partial.html', context)
    
@login_required
def task_create(request):
    form = TaskCreateForm(request.POST or None)
    if request.method == 'POST':
        task = form.save(commit=False)
        task.user = request.user
        if form.is_valid():
            task.save()
            messages.success(request, 'Task created successfully')
    tasks = SimpleTask.objects.filter(user=request.user).order_by('completed', '-updated_at')
    context = get_paginated_tasks(request, tasks, 5)
    return render(request, 'partials/task_list_partial.html', context)

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    form = UserUpdateForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            # Update user
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
    messages.success(request, 'Profile updated successfully')
    return render(request, 'partials/profile.html', {'profile_user': user, 'form': form})