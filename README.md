Django project template
=======================

This is a set of default templates for Django projects, based on the
reccomendations of the [Two Scoops of Django](http://2scoops.org/) book,
especially for the structure of the settings. Make sure you use the correct
branch for your project according to the version of Django you're using.

This branch contains a template for the [Mezzanine
CMS](http://mezzanine.jupo.org/). Instead of using the Django 1.3 structure
created by the `mezzanine-project` script, it uses the post-1.3 structure.

To create a new project using this template, do the following:

    pip install mezzanine
    django-admin.py startproject --template=https://github.com/sephii/django-project-template/archive/mezzanine.zip myproject
    cd myproject
    pip install -r requirements/dev.txt
    echo "sqlite:///myproject.sqlite" > envdir/local/DATABASE_URL
    python manage.py createdb
    python manage.py runserver

You can now start hacking!

Default settings supported via envdir
-------------------------------------

* ALLOWED_HOSTS (1 host / line)
* DATABASE_URL
* NEVERCACHE_KEY
* SECRET_KEY
* STATIC_ROOT

The `DATABASE_URL` is set using
[DJ-Database-URL](https://github.com/kennethreitz/dj-database-url). You'll find
examples for the different connectors on the project page but here's a short
list for convenience:

* MySQL: mysql://user:password@host/database
* PostgreSQL: postgres://user:password@host/database
* SQLite: sqlite:////absolute/path/to/db/file or sqlite:///relative/path/to/db/file

Also don't forget to install the related database driver if you use anything
else than SQLite (MySQL-python for MySQL, psycopg2 for PostgreSQL).
