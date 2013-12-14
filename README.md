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

    django-admin.py startproject --template=https://github.com/sephii/django-project-template/archive/mezzanine.zip myproject
    cd myproject
    pip install -r requirements/dev.txt
    echo "postgres://user:password@database" > envdir/local/DATABASE_URL
    python manage.py syncdb --all
    python manage.py runserver

You can now start hacking!
