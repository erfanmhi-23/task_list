from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasklistview, name='task-list'),
    path('create/', views.taskcreateview, name='task-create'),
    path('<int:pk>/update/', views.taskupdateview, name='task-update'),
    path('<int:pk>/archive/', views.taskarchiveview, name='task-archive'),
]
