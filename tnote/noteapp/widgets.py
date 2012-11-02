from django.conf import settings
from django.forms import widgets


class DynamicAmountOfSymbols(widgets.Textarea):
    class Media:
        js = (
        settings.STATIC_URL + "js/jquery-1.8.2.min.js",
        settings.STATIC_URL + "js/js_amount_of_symbols.js",
        )

    def __init__(self, *args, **kwargs):
        attrs = kwargs.setdefault('attrs', {})
        attrs.setdefault('cols', '100')
        attrs.setdefault('rows', '10')
        super(DynamicAmountOfSymbols, self).__init__(*args, **kwargs)
