from django import forms
from django.core.validators import MinLengthValidator
from tnote.noteapp.models import Entry, Imgfile


class AddForm(forms.ModelForm):
    class Meta:
        model = Entry


class AddImage(forms.ModelForm):
    class Meta:
        model = Imgfile

    def __init__(self, *args, **kwargs):
        super(AddImage, self).__init__(*args, **kwargs)
        self.fields['imagefile'].widget.attrs['onchange'] = 'tstFile(this)'
