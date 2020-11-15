# -*- coding: utf-8 -*-
# see also https://blog.godatadriven.com/setup-py
# python setup.py sdist bdist_wheel
#


from setuptools import setup, find_packages

setup(
    name='ndview',
    version='0.01dev',
    description='Multidimensional array viewer widget for jupyter',
    author='jlab.berlin',
    url='https//github.com/danionella/ndview',
    packages=['ndview', ], #find_packages(include=['exampleproject', 'exampleproject.*']),
    license='mit',
    python_requires='>=3.5',
    install_requires=['matplotlib', 'ipywidgets', 'ipympl', 'numpy']
)
