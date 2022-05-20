django-admin-async-upload
===============================

.. image:: https://api.travis-ci.org/jonatron/django-admin-resumable-js.svg?branch=master
   :target: https://travis-ci.org/jonatron/django-admin-resumable-js

django-admin-async-upload is a django app to allow you to upload large files from within the django admin site asynchrously (using ajax), that means that you can add any number of files on the admin page (e.g. through inline models) and continue editing other fields while files are uploading.

django-admin-async-file-uploads is compatible with django-storages (tested with S3Storage)


Screenshot
----------

#TODO: update this screenshot

.. image:: https://github.com/jonatron/django-admin-resumable-js/raw/master/screenshot.png?raw=true


Installation
------------

* pip install django-admin-async-upload
* Add ``admin_async_upload`` to your ``INSTALLED_APPS``
* Add ``from django.urls import path, include, re_path`` to your urls.py
* Add ``re_path(r'^admin_async_upload/', include('admin_async_upload.urls')),`` to your urls.py
* Add a model field eg: ``from admin_async_upload.models import AsyncFileField``

::

    class Foo(models.Model):
        bar = models.CharField(max_length=200)
        foo = AsyncFileField()



Optionally:

* Set ``ADMIN_RESUMABLE_CHUNKSIZE``, default is ``"1*1024*1024"``
* Set ``ADMIN_RESUMABLE_STORAGE``, default is setting of DEFAULT_FILE_STORAGE and ultimately ``'django.core.files.storage.FileSystemStorage'``.  If you don't want the default FileSystemStorage behaviour of creating new files on the server with filenames appended with _1, _2, etc for consecutive uploads of the same file, then you could use this to set your storage class to something like https://djangosnippets.org/snippets/976/
* Set ``ADMIN_RESUMABLE_CHUNK_STORAGE``, default is ``'django.core.files.storage.FileSystemStorage'`` .  If you don't want the default FileSystemStorage behaviour of creating new files on the server with filenames appended with _1, _2, etc for consecutive uploads of the same file, then you could use this to set your storage class to something like https://djangosnippets.org/snippets/976/
* Set ``ADMIN_RESUMABLE_SHOW_THUMB``, default is False. Shows a thumbnail next to the "Currently:" link.
* Set ``ADMIN_SIMULTANEOUS_UPLOADS`` to limit number of simulteneous uploads, dedaults to `3`. If you have broken pipe issues in local development environment, set this value to `1`.


Versions
--------





Compatibility
-------------

Tested on Django 2.2 running on python 3.6 and 3.7
Updated for Django 4

Thanks to
---------

original django-admin-resumable-js by jonatron https://github.com/jonatron/django-admin-resumable-js 

django-admin-resumable-js fork by roxel https://github.com/roxel/django-admin-resumable-js (django-admin-async-upload is based on this fork 

Resumable.js https://github.com/23/resumable.js

django-resumable https://github.com/jeanphix/django-resumable


