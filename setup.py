#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:       Alisue
# Last Change:  18-Mar-2011.
#
from setuptools import setup
from setuptools import find_packages
from packageutils.version import get_git_version

version = get_git_version()

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="django-package-skeleton",
    version=version,
    description = "Skeleton package of Django App Package",
    long_description=read('README.rst'),
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django signals object field relation generic",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-observer",
    download_url = r"https://github.com/lambdalisue/django-observer/tarball/master",
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires = (
        'distribute',
        'setuptools-git',
    ),
    tests_require = (
        'PyYAML',
        'django',
    ),
    test_suite='packageutils.runtests.runtests',
)
