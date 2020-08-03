from django import forms

# This newly defined class, descendant of the Form species, will contain:
# A data field called item, which will map to an SQL database once filled, and
# A widget, which contains all that's needed to stand in for an HTML input element:


class ToDoListForm(forms.Form):
    item = forms.CharField(
        max_length=45,
        widget=forms.TextInput(
            # this widget is pretty much going to be an input (in fact I'll bet it is, in its heart, an HTML text input)
            # so we can give it all the attributes (attrs) that our input element would have:
            attrs={
                "class": "add-item",
                "placeholder": "write somethin' down eh??",
                "aria-label": "Todo",
                "aria-describeby": "add-btn",
            }
        ),
    )

