from django.urls import path
from . import  views

urlpatterns = [
    path("todolist/create/", views.todolist_create, name = "todolist_create"),
    path("todolist/", views.todolist_read, name = "todolist_read"),
    path("todolist/delete/<int:todo_id>/", views.todolist_delete, name = "todolist_delete"),
    path("todolist/<int:todo_id>/", views.todolist_update, name = "todolist_update"),
]
