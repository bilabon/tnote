from django import forms
from django.core.validators import MinLengthValidator
from tnote.noteapp.models import *
from tnote.noteapp.widgets import DynamicAmountOfSymbols


class AddForm(forms.ModelForm):
    text = forms.CharField(widget=DynamicAmountOfSymbols())

    class Meta:
        model = Entry
