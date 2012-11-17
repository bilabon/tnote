from django import forms
from django.core.validators import MinLengthValidator
from tnote.noteapp.models import *
from tnote.noteapp.widgets import DynamicAmountOfSymbols


class AddForm(forms.ModelForm):
    text = forms.CharField(widget=DynamicAmountOfSymbols())

    class Meta:
        model = Entry
        fields = ('text',)

    def clean(self):
        data = self.cleaned_data
        msg_error = u'Your note must be at least 10 characters.'
        try:
            if len(data['text']) >= 10:
                return self.cleaned_data
            else:
                raise forms.ValidationError(msg_error)
        except KeyError:
            raise forms.ValidationError(msg_error)
