from os import getcwd
from os.path import join
from setuptools import setup

setup(
    name="testDirectoryCreation",
    author="Tyler Danstrom",
    email="tdanstrom@uchicago.edu",
    packages=["testDirectoryCreation"],
    short_description="A simple utility for creating a temporary directory full of specific files",
    long_description=open(join("./", 'README.md'), 'r', encoding='utf-8').read()
)