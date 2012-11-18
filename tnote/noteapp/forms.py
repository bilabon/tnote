from django import forms
from tnote.noteapp.widgets import DynamicAmountOfSymbols
from tnote.noteapp.models import *


class AddForm(forms.ModelForm):
    text = forms.CharField(widget=DynamicAmountOfSymbols())

    class Meta:
        model = Entry
        fields = ('text',)

    def clean(self):
        cleaned_data = super(AddForm, self).clean()
        text = cleaned_data.get("text")
        try:
            len(text)
        except TypeError:
            msg_error = u'Your note must be at least 10 characters.'
            self._errors["text"] = self.error_class([msg_error])
            return cleaned_data

        if len(text) < 10:
            msg_error = u'Your note must be at least 10 characters.'
            self._errors["text"] = self.error_class([msg_error])
            del cleaned_data["text"]
        return cleaned_data
