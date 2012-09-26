from django.db import models
from .widgets import WygiwygEditorWidget

__all__ = (
    'HtmlField',
)

class HtmlField(models.TextField):
    """
    A large string field for HTML content.
    It uses the installed WYSIWYG editor (e.g. TinyMCE or CKEditor) in forms.
    """
    def formfield(self, **kwargs):
        from .forms import WygiwygEditorField
        defaults = {
            'form_class': WygiwygEditorField,
            'widget': WygiwygEditorWidget
        }
        defaults.update(kwargs)

        return super(HtmlField, self).formfield(**defaults)


# Tell South how to create custom fields
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [
        "^any_htmlfield\.models\.HtmlField",
    ])
except ImportError:
    pass


# Tell the Django admin it shouldn't override the widget because it's a TextField
from django.contrib.admin import options
options.FORMFIELD_FOR_DBFIELD_DEFAULTS[HtmlField] = {'widget': WygiwygEditorWidget}
