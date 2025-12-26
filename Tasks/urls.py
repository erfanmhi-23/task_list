from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskArchiveView

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('archive/<int:pk>/', TaskArchiveView.as_view(), name='task-archive'),
]
