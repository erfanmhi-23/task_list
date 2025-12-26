from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks
from django.urls import reverse_lazy

class TaskListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user.profile, is_archived=False).order_by('-created_at')

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'status', 'priority', 'deadline']

    def form_valid(self, form):
        form.instance.owner = self.request.user.profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'status', 'priority', 'deadline']

    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user.profile)

    def get_success_url(self):
        return reverse_lazy('task-list')

class TaskArchiveView(LoginRequiredMixin, UpdateView):
    model = Tasks
    template_name = 'tasks/task_list.html'
    fields = []

    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user.profile)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.is_archived = True
        task.save()
        return redirect('task-list')
