Introduction
============

The ``wysiwyg_editor`` package offers a switchable WYSIWYG editor in Django forms and the admin interface.

By using this package instead of a specific WYSIWYG editor for your Django package,
it gives end-developers the choice to use their preferred WYSIWYG editor for their applications.


API example
===========

::

    from django.db import models
    from wysiwyg_editor.models import HtmlField

    class Article(models.Model):
        title = models.CharField(max_length=200)
        content = HtmlField()


Installation
============

First install the module, and a accompanying WYSIWYG editor package.
It can be installed from PyPI:


Using CKEditor
--------------

To use CKEditor, install::

    pip install django-wysiwyg-editor django-ckeditor

And configure it::

    INSTALLED_APPS += (
        'wysiwyg_editor',
        'ckeditor',
    )

And complete the configration of django-ckeditor_::

    CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

And the required URLs::

    urlpatterns += patterns('',
        url(r'^ckeditor/', include('ckeditor.urls')),
    )


Using TinyMCE
-------------

To use TinyMCE, install::

    pip install django-wysiwyg-editor django-tinymce

And configure it::

    INSTALLED_APPS += (
        'wysiwyg_editor',
        'tinymce',
    )

And complete the configuration of django-tinymce_::

    urlpatterns += patterns('',
        url(r'^tinymce/', include('tinymce.urls')),
    )


Changelog
=========

Version 0.1: initial release.


Credits
=======

* The idea of this package is based on django-wysiwyg_
  which implements this idea as a template tag.

.. _django-ckeditor: https://github.com/shaunsephton/django-ckeditor
.. _django-tinymce: https://github.com/aljosa/django-tinymce
.. _django-wysiwyg: https://github.com/pydanny/django-wysiwyg
