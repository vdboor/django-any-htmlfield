#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join
import sys, os

setup(
    name='django-wysiwyg-editor',
    version='0.1.0',
    license='Apache License, Version 2.0',

    install_requires=[],
    extras_require = {
        'tinymce': ['django-tinymce'],
        'ckeditor': ['django-ckeditor'],
    },
    description='A WYSIWYG editor field for Django, allowing to select between WYSIWYG editors easily (for example CKEditor or TinyMCE).'
    long_description=open('README.rst').read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-wysiwyg-editor',
    download_url='https://github.com/edoburu/django-wysiwyg-editor/zipball/master',

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
