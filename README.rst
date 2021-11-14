Feron
=====

The management platform that powers Feron Auto Management Company, a hire purchase service company for automobiles.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified, use the default phone no +2348110258116, contact the CTO for the OTP code, input it in the next page for verification and ready to go.

* To create an **superuser account**, use this command::

    python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  mypy feron

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    coverage run -m pytest
    coverage html
    open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Setup
^^^^^

* On project initialisation, clone the repository using

    git clone https://github.com/Feron-Auto/feron.git

* *Note:* This needs to be done only once


Create and activate virtual environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After creating a virtual environment (optional), activate it by running ::

    python -m venv env


For windows, activate it this way ::


    env/Scripts/activate


For other operating system like Linux and MacOS, use ::


    source env/bin/activate


Installing project dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the project dependencies, use ::

    pip install -r requirements/local.txt


Migrating changes
^^^^^^^^^^^^^^^^^
First migration should be as follows ::


    python manage.py makemigrations users driver investor vehicle


In consequent times make sure you run the following code after creating either a new django app, model or migration. This will ensure that the database is in sync and prevent unnecessary issues. ::

    python manage.py makemigrations

    python manage.py migrate

Should you encounter any data migration issues
run: ::


    python manage.py migrate --run-syncdb

**Note**: You can skip the above steps just after creating your virtual environment by using the automated script `scripts/setup.sh` file. or running it in the terminal ::


    ./scripts/setup.sh


* Before creating any change, go to Github projects_  and pick a card, **assign the ticket to yourself** and move it to the **In progress** column then create a new branch in the format below
    .. _projects: https://github.com/Feron-Auto/feron/projects/1

    * Feron-<issue-no>/short-description-without-space

    * e.g. Feron-10/Investor-Main-Dashboard

* After completion, commit your changes using the code command below ::

    git add .
    git commit -m "commit messsge"


once finished, push your branch to the repository and create a `new pull request` then move to the **code review** column ::

    git push -u origin HEAD


You can skip the terminal by using GitHub Desktop



Before deleting database
^^^^^^^^^^^^^^^^^^^^^^^^

Please before deleting your database, **make a backup** unless you don't mind recreating data from the beginning. use the following command to backup your data ::


    python manage.py dumpdata ../local.json

To restore your data, run the following command ::

    python manage.py loaddata --exclude auth.permission --exclude contenttypes ../local.json


If you get an error, go a folder back and open `local.json`. If the file doesn't end with a `]`, please add it and rerun the code.


Django commands
^^^^^^^^^^^^^^^

There are commands that can make development very easier. To find them out, run the following in the terminal ::

    python manage.py


Generating test data
^^^^^^^^^^^^^^^^^^^^

To generate test data, run the following command: ::

    python manage.py create_<model_name_in_lowercase>


you can also provide an optional amount of models to generate by passing the `-a` or `--amount` command followed by how many you need to generate. For example ::

    python manage.py create_investor -a 5
    python manage.py create_vehicle --amount 10
    python manage.py create_vehicle # this one requires no argument



Viewing the list of available urls from the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
 ::

    python manage.py list_urls


To filter the urls by certain keywords, use either of the two options below

**Option 1** ::

    python manage.py list_urls | grep <keyword>


**Option 2** ::

    python manage.py list_urls -c <keyword>  or
    python manage.py list_urls --contains <keyword>



Note:
----------

1. You are not allowed to make changes to the main branch
2. Environment variable should not be used directly, rather use the os.getenv("THE_VARIABLE_NAME")
3. Make comment on the environment variable when making a commit
4. Exclude your branch migration folder before making a commit
