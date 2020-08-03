from django.urls import path
from . import views


# URL PATTERNS: These would be like the endpoints in an Express engine, except that their GET/POST/whatever statuses
# Are defined by the view functions that supply their second arguments (the first arg being their url path name):
urlpatterns = [
    path("", views.index, name="homepage"),
    path("add", views.addToDoItem, name="add"),
    path("completeToDo/<id>", views.completeToDo, name="completeToDo"),
    path("deleteCompleted", views.deleteCompleted, name="deleteCompleted"),
    path("deleteAll", views.deleteAll, name="deleteAll"),
]

