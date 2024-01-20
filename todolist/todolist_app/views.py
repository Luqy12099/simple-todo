from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .form import form_create
from .models import ToDoList

#region ================================= TODOLIST AREA ==========================================================================

@login_required()
def todolist_create(response):
    if response.method =="POST":
        form = form_create(response.POST)
        if form.is_valid():
            instance = form.save(commit=False)  # Prevent premature saving
            instance.user = response.user  # Assign the current user to the 'user' field
            instance.save()
            return redirect('todolist_read')
    else:
        form = form_create()
    return render(response, "todolist_app/todolist_create.html", {"form":form})

@login_required()
def todolist_read(response):
    data = ToDoList.objects.filter(user=response.user)
    return render(response, "todolist_app/todolist_read.html", {"data":data})

@login_required()
def todolist_delete(response, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id)
    print('abc')

    # Check if the user has permission to delete this ToDoList item
    if response.user == todo.user or todo == None:
        todo.delete()

    return redirect('todolist_read')

@login_required()
def todolist_update(response, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id)

    # Check if the user has permission to delete this ToDoList item
    if response.user == todo.user:
        if response.method == 'POST':
            new_name = response.POST.get('name')
            todo.name = new_name
            todo.save()
            return render(response, "todolist_app/todolist_edit.html", {"todo":todo})
        else:
            return render(response, "todolist_app/todolist_edit.html", {"todo":todo})

    return redirect('todolist_read')

#endregion ================================= TODOLIST AREA ==========================================================================
