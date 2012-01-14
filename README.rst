Django Application Package Skeleton

The following features exists

-   Testing demo django test project with ``setup.py``

-   Add Django apps required to execute test dynamically

-   Automatically update the version number with git

How to use
====================

1.  Falk this project in your github

2.  Rename ``package`` directory as your app name and fix ``setup.py`` as you want

3.  Add your app in ``INSTALL_APPS`` in ``tests/settings.py``


Testing demo django test project with ``setup.py``
====================================================================================================
There is a simple blog django project in ``tests`` directory so just modify the project as you want
and add::

    $ python setup.py test

will run the project tests


Add Django apps required to execute test dynamically
======================================================================================================
If your Django app required apps just for testing then you can use ``app_testcase.AppTestCase`` to add
any django app dynamically in test

If you create some django field app and you want to test the field with simple ``Book`` model then you
can

1.  Create an simple app called ``yourfieldname/tests/apps/books``

2.  Create simple book models in ``yourfieldname/tests/apps/books/models.py``

3.  Use ``yourfieldname.tests.app_testcase.AppTestCase`` insted of ``django.test.TestCase`` and add ``yourfieldname.tests.apps.books`
    in ``install_apps`` field of test case::

        from app_testcase import AppTestCase
        
        class YourFieldTestCase(AppTestCase):
            install_apps = [
                'yourfieldname.tests.apps.books',
            ]
            # write your tests


Automatically update the version number with git
================================================================================================
The original idea came from http://dcreager.net/2010/02/10/setuptools-git-version-numbers/

What you need to do is

1.  Add annotated or signed tag with the following command::

        $ git tag -a 0.1

2.  Then your ``git describe`` shows the tag name and ``python setup.py sdist``
    create the tag named version package

3.  If you change anything and commit, your ``git describe`` may change and that
    is used as new version number and it become miner version up

4.  Add new annotated or signed tag when you release stable version.
