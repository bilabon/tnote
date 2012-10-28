from django.conf import settings
from django.forms import widgets
from django.utils.safestring import mark_safe


class DynamicAmountOfSymbols(widgets.Textarea):
    class Media:
        js = (
        #"http://code.jquery.com/jquery-latest.js",
        settings.STATIC_URL + "js/jquery-1.8.2.min.js",
        settings.STATIC_URL + "js/js_of_noteapp.js",
        )

    def __init__(self, attrs=None):
        default_attrs = {'cols': '100', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
        super(DynamicAmountOfSymbols, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        output = super(DynamicAmountOfSymbols, self).render(name, value, attrs)
        output += "</br>test output"
        return mark_safe(output)
