from django.views.generic import DetailView, UpdateView ,ListView
from Tasks.models import Tasks
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'timezone']
    template_name = 'accounts/profile_form.html'

    def get_object(self):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy('profile-detail')


class ProfileTaskListView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'accounts/profile_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Tasks.objects.filter(owner=self.request.user.profile, is_archived=False)
