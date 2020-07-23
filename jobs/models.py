from django.db import models

# Create your models here.
class ToDoList(models.Model):
    item = models.CharField(max_length=66)
    completed = models.BooleanField(default=False)

    # "Built-in" object method lets us use the object as a string/tells which attribute to use if we want to, say, print this object:
    def __str__(self):
        return self.item


# class NumberWang(models.Model):
#     wangernum = models.IntegerField()
#     numberwang = models.BooleanField(default=False)

#     def __str__(self):
#         return self.wangernum
