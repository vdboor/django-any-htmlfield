from django import forms
from wysiwyg_editor.widgets import WygiwygEditorWidget


class WygiwygEditorField(forms.CharField):
    """
    A form field that displays a WYSIWYG editor.
    """
    widget = WygiwygEditorWidget
