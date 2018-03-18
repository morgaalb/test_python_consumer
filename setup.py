#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="test_python_consumer",
    version="0.2",
    scripts=["test_python_consumer_script.py"],
    dependency_links=[
        "git+https://github.com/morgaalb/test_python_package.git#egg=test_python_package-0.2"
    ],
    install_requires=["test_python_package>=0.2"]
)