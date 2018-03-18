#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="test_python_consumer3",
    version="0.2",
    scripts=["test_python_consumer_script.py"],
    dependency_links=[
        #"https://github.com/morgaalb/test_python_package/tarball/master@master#egg=test_python_package-0.2"
        "git+https://github.com/morgaalb/test_python_package.git#egg=test_python_package-0.2"
    ],
    install_requires=["test_python_package>=0.2"]
)