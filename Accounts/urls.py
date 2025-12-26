from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, ProfileTaskListView

urlpatterns = [
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/tasks/', ProfileTaskListView.as_view(), name='profile-tasks'),
]
