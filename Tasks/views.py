from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tasks
from .forms import TaskForm

@login_required
def tasklistview(request):
    tasks = Tasks.objects.filter(owner=request.user.profile, is_archived = False).order_by("-created_at")
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def taskcreateview(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user.profile
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def taskupdateview(request, pk):
    task = get_object_or_404(Tasks, pk=pk, owner=request.user.profile)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def taskarchiveview(request, pk):
    task = get_object_or_404(Tasks, pk=pk, owner=request.user.profile)
    task.is_archived = True
    task.save()
    return redirect('task-list')
