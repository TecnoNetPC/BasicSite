from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    path('delete_task/<int:id>', views.delete_task, name="delete_task"),
    path('true_task/<int:id>', views.true_task, name="true_task"),
    path('delete_project/<int:id>', views.delete_project, name="delete_project"),
]
