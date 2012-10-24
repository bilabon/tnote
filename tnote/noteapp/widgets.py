from django import forms
from django.conf import settings
from django.forms import Textarea


class DynamicAmountOfSymbols(forms.Textarea):
    class Media:
        js = (
        #"http://code.jquery.com/jquery-latest.js",
        settings.STATIC_URL + "js/jquery-1.8.2.min.js",
        settings.STATIC_URL + "js/js_of_noteapp.js",
        )

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', '100')
        attrs.setdefault('rows', '10')
        super(DynamicAmountOfSymbols, self).__init__(*args, **kwargs)
