from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example of python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='http//github.com/blah/blah',
    author='<Yoda>',
    author_email='<yoda@starwars.com>'
)