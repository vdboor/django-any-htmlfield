from django.contrib.admin.widgets import AdminTextareaWidget
from django.db import models


class HtmlField(models.TextField):
    """
    A large string field for HTML content.
    It uses the installed WYSIWYG editor (e.g. TinyMCE or CKEditor) in forms.
    """
    def formfield(self, **kwargs):
        from .forms import WygiwygEditorField
        from .widgets import WygiwygEditorWidget
        defaults = {
            'form_class': WygiwygEditorField,
            'widget': WygiwygEditorWidget
        }
        defaults.update(kwargs)

        # Override the enforced admin widget with some sanity.
        if defaults['widget'] is AdminTextareaWidget:
            defaults['widget'] = WygiwygEditorWidget

        return super(HtmlField, self).formfield(**defaults)


# Tell South how to create custom fields
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [
        "^wysiwyg_editor\.models\.HtmlField",
    ])
except ImportError:
    pass
