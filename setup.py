#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-any-htmlfield',
    version='0.1.0',
    license='Apache License, Version 2.0',

    install_requires=[],
    extras_require = {
        'tinymce': ['django-tinymce'],
        'ckeditor': ['django-ckeditor'],
        'imperavi': ['django-imperavi'],
        'clean-html5lib': ['html5lib'],
        'clean-pytidylib': ['pytidylib'],
    },
    description='A WYSIWYG HTML editor field for Django, allowing to select between WYSIWYG editors easily (for example CKEditor, Radactor or TinyMCE).',
    long_description=open('README.rst').read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-any-htmlfield',
    download_url='https://github.com/edoburu/django-any-htmlfield/zipball/master',

    packages=find_packages(),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
