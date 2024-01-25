from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .form import form_create
from .models import ToDoList, Item
from django.http import JsonResponse, HttpResponseForbidden
from django.db import transaction

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
    # Check if the user has permission to delete this ToDoList item
    if response.user == todo.user or todo == None:
        todo.delete()

    return redirect('todolist_read')

@login_required()
def todolist_update(response, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id)
    items = Item.objects.filter(todolist=todo)

    # Check if the user has permission to delete this ToDoList item
    if response.user == todo.user:
        if response.method == 'POST':
            new_name = response.POST.get('todo_name')
            if new_name != None: 
                todo.name = new_name
                todo.save()
            return render(response, "todolist_app/todolist_edit.html", {"todo":todo, "items":items})
        else:
            return render(response, "todolist_app/todolist_edit.html", {"todo":todo, "items":items})

    return redirect('todolist_read')

#endregion ================================= TODOLIST AREA ==========================================================================

#region ================================= ITEM AREA ==========================================================================
@login_required()
def item_create(response):
    todo_id  = response.POST.get('todo_id')
    todo = get_object_or_404(ToDoList, id=todo_id)

    if response.user == todo.user and response.method == 'POST':
        new_item_text = response.POST.get('text')
        if new_item_text:
            Item.objects.create(todolist=todo, text=new_item_text, complete=False)

    return redirect('todolist_update', todo_id=todo_id)


@login_required()
def item_update(response):
    if response.method == 'POST':
        item_id = response.POST.get('item_id')
        is_checked = response.POST.get('is_checked')
        new_text = response.POST.get('item_text')

        item = get_object_or_404(Item, id=item_id)
        todo_id = item.todolist.id
        
        if new_text != None:
            item.text = new_text

        if is_checked != None:
            is_checked = (response.POST.get('is_checked') != 'True')
            item.complete = is_checked

        item.save()

        return redirect('todolist_update', todo_id=todo_id)

    

@login_required()
def item_delete(response, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.todolist and response.user == item.todolist.user:
        try:
            with transaction.atomic():
                todo_id = item.todolist.id
                item.delete()
                return redirect('todolist_update', todo_id=todo_id)
        except Exception as e:
            print(f"Error deleting item: {e}")
    else:
        return HttpResponseForbidden("You don't have permission to delete this item.")


#endregion ================================= ITEM AREA ==========================================================================
