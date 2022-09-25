from django import forms
from django.contrib.postgres.search import SearchVector

from .models import Comment


class EmailPostForm(forms.Form):
    """Returns the email form."""

    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """Return form with name, email, and body."""

    class Meta:
        """Use three fields from Comment class to generate form."""

        model = Comment
        fields = ["name", "email", "body"]


class SearchForm(forms.Form):
    """Return search form."""

    query = forms.CharField(max_length=100)
