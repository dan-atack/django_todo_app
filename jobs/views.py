from django.shortcuts import render
from .models import ToDoList

# Create your views here.


def index(req):

    todo_items = ToDoList.objects.order_by("id")
    context = {"todo_items": todo_items}
    return render(req, "jobs/index.html", context)

