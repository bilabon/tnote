from django import forms
from django.core.validators import MinLengthValidator
from tnote.noteapp.models import *


class AddForm(forms.ModelForm):
    class Meta:
        model = Entry
