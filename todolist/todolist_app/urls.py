from django.urls import path
from . import  views

urlpatterns = [
    path("todolist/create/", views.todolist_create, name = "todolist_create"),
    path("todolist/", views.todolist_read, name = "todolist_read"),
    path("todolist/delete/<int:todo_id>/", views.todolist_delete, name = "todolist_delete"),
    path("todolist/<int:todo_id>/", views.todolist_update, name = "todolist_update"),
    path("item/create/", views.item_create, name = "item_create"),
    path("item/update/", views.item_update, name = "item_update"),
    path("item/delete/<int:item_id>/", views.item_delete, name = "item_delete"),
]
