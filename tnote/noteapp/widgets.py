from django import forms
from django.conf import settings


class DynamicAmount(forms.Textarea):
    """
    Custom widget thet extends textarea widget and show dynamically amount
    of symbols are writed in field.
    """
    class Media:
        js = (
              settings.STATIC_URL + "js/jquery-1.8.2.min.js",
              settings.STATIC_URL + "js/count_of_notes.js",
              )

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', '100')
        attrs.setdefault('rows', '10')
        super(DynamicAmount, self).__init__(*args, **kwargs)
