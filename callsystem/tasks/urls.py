from django.urls import path
from . import views


urlpatterns = [
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('task/', views.create_task, name='create_task'),
]

