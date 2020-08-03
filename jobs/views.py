from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ToDoListForm
from django.views.decorators.http import require_POST

# Create your views here.

# This function is called whenever a user arrives (does a get) to the root directory of the site in urls.py:
def index(req):
    # First we create a variable that takes all of the ToDoList objects and makes them into a list, in order of their ids:
    todo_items = ToDoList.objects.order_by("id")
    # Next, we create a variable called form that is an instance of the ToDoListForm class:
    form = ToDoListForm()
    # Then we make a CONTEXT dictionary, which lets us connect these variables to KEYS - words that we can inject into our HTML template:
    context = {"todo_items": todo_items, "form": form}
    # Lastly, we render, in response to the req, the index.html template page, and give it the context dictionary to feed into our
    # marked up areas with the EJS-esque syntax:
    return render(req, "jobs/index.html", context)


# This function is called when submit button for the input widget is hit; urls.py routes the post, and ONLY THE POST to this function:
@require_POST
def addToDoItem(req):
    # Create a variable to store the request's POST:
    form = ToDoListForm(req.POST)
    # if it's all good according to the is_valid() function,
    if form.is_valid():
        # Create a new instance of the ToDoList MODEL Class, and make its item attribute equal to the req's POST's item attribute
        # (both form and db model have obviously been made in the same shape... hey wait a minute!)
        new_todo_item = ToDoList(item=req.POST["item"])
        # Now save that item to the DB (all models have a built-in save function):
        new_todo_item.save()
    # No quotes around 'index' - you can return the function directly:
    return redirect(index)


# Function for displaying completed items:


def completeToDo(req, id):
    # Get the desired item by matching the ID supplied as an argument to this function (note that there is now an id as well as a req),
    # and saving it as the variable, todo.
    # See how we use the imported ToDoList model's objects' get METHOD and give it (pk=id) as its argument;
    # This means, 'use the id given as an argument to this function as the PK (Primary Key) of the ToDoList object to be retrieved':
    todo = ToDoList.objects.get(pk=id)
    # Once we have the item selected, set its completed attribute to True (all items start with completed = False):
    todo.completed = True
    # Then, use the built-in save method to update the database with this change:
    todo.save()
    # Finally, redirect back to the index page to trigger a refresh:
    return redirect(index)


def deleteCompleted(req):
    # First we'll query the DB for all the ToDoList objects that have an * __exact * match for their 'completed' attribute = True',
    # Then, on the same line, we use the delete() method:
    ToDoList.objects.filter(completed__exact=True).delete()
    return redirect(index)


def deleteAll(req):
    # Pretty straightforward since we're not doing any filtering; just get ALL of the ToDoList model's objects, AND NEUTRALIZE THEM.
    # One crucial little thing to note: ALL here refers to an object METHOD, so we must execute it before running the delete METHOD:
    ToDoList.objects.all().delete()
    return redirect(index)
