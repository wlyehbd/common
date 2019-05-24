#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='zhuge-common',
    version="1.1.76",
    packages=find_packages(exclude=["apps"]),
    description=(
        '诸葛找房data部门'
    ),
    long_description='',
    author='lucas',
    author_email='lutaixiang@zhuge.com',
    maintainer='hanbingde',
    maintainer_email='hanbingde@zhuge.com',
    # license='BSD License',
    # py_modules=['apps'],
    platforms=["all"],
    url='https://git.zhugefang.com/DataAPI/zhuge_common',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[]
)
