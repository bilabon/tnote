from django import forms
from django.forms import ImageField
from tnote.noteapp.widgets import DynamicAmountOfSymbols
from tnote.noteapp.models import *


class AddForm(forms.ModelForm):
    text = forms.CharField(widget=DynamicAmountOfSymbols())

    class Meta:
        model = Entry
        fields = ('text', 'imagefile', )

    def clean(self):
        cleaned_data = super(AddForm, self).clean()
        text = cleaned_data.get("text")

        try:
            self.cleaned_data['imagefile']
        except KeyError:
            msg_error = u'Some error with your image.'
            self._errors["imagefile"] = self.error_class([msg_error])

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
