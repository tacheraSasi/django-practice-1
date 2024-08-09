from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import TodoItem
from .forms import TodoItemForm

# my todo app views goes here

def index(request):
    todo_items = TodoItem.objects.all()
    num = todo_items.count()
    context = {"todo_items":todo_items,"number_of_todos":num}
    return render(request,"todo/index.html",context)


def addTodo(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo-home")
    context = {"form":TodoItemForm(),}
    return render(request,"todo/add.html",context)


def updateTodo(request,pk):
    todo = TodoItem.objects.get(id = pk)
    if todo:
        if request.method == "POST":
            form = TodoItemForm(request.POST,instance=todo)
            if form.is_valid():
                form.save()
                return redirect("todo-home")
    else:
        return HttpResponse("todo does not exist")
    context = {"form":TodoItemForm(instance=todo),}
    return render(request,"todo/update.html",context)


def deleteTodo(request,pk):
    todo = TodoItem.objects.get(id = pk)
    if todo:
        todo.delete()
        return redirect("todo-home")
    else:
        return HttpResponse("Invalid request")
