from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "todo-home"),
    path("add/",views.addTodo,name = "add-todo"),
    path("update/<str:pk>", views.updateTodo,name = "update-todo"),
    path("delete/<str:pk>", views.deleteTodo,name = "delete-todo"),

]