# setup.py
from setuptools import setup
from Cython.Build import cythonize

import os

os.environ['CC'] = 'aarch64-linux-gnu-gcc'
os.environ['LDSHARED'] = 'aarch64-linux-gnu-gcc -shared'


setup(
    name="cython-test",
    ext_modules=cythonize("sum_of_squares.pyx", language_level=3),
    py_modules=["sum_of_squares"],  # Explicitly state the module
    zip_safe=False,
)