from django.conf import settings


# Import the rich text editor backend
if 'ckeditor' in settings.INSTALLED_APPS:
    from ckeditor.widgets import CKEditorWidget as WygiwygEditorBase
elif 'tinymce' in settings.INSTALLED_APPS:
    from tinymce.widgets import AdminTinyMCE as WygiwygEditorBase
else:
    # Fallback to HTML, provide hook to attach RTE yourself.
    from django.forms.widgets import Textarea as WygiwygEditorBase


class WygiwygEditorWidget(WygiwygEditorBase):
    """
    A WYSIWYG editor widget that switches to the installed editor automatically.
    """

    def __init__(self, attrs=None):
        # Formalize constructor for the widget.
        # TODO: find a good way to pass custom settings, while preserving the backend switching functionality
        # CKEditor uses a "config_name" (good)
        # TinuyMCE passes attributes directly, so needs a "config_name" indirection.

        final_attrs = {'class': 'vLargeTextField any-htmlfield'}
        if attrs is not None:
            final_attrs.update(attrs)

        super(WygiwygEditorWidget, self).__init__(attrs=final_attrs)
