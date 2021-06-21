#-*- coding:utf-8 -*-

"""
Created on 2020/03/03
------
@author: Chao Li; Mengshi Dong
Email:  lichao19870617@gmail.com; dongmengshi1990@163.com
"""

from setuptools import setup, find_packages

with open("README_pypi.md", "r") as fh:
    long_description = fh.read()

setup(
    name='eslearn',
    version='1.1.5',
    description=(
        'This project is designed for machine learning in resting-state fMRI field'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chao Li; Mengshi Dong',
    author_email='lichao19870617@gmail.com',
    maintainer='Chao Li; Mengshi Dong',
    maintainer_email='lichao19870617@gmail.com',
    license='MIT License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/easylearn-fmri/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],

    install_requires=[
        "imbalanced-learn",
        "joblib",
        "requests",
        "matplotlib",
        "nibabel",
        "openpyxl",
        "xlrd==1.2.0",
        "pandas",
        "PyQt5",
        "PyQt5-sip",
        "python-dateutil",
        "scikit-learn",
        "numpy==1.18.5",
        "scipy",
        'seaborn',
        'requests',
        'progressbar',
        "tensorflow==2.3.0",
        "netron",
    ],

    include_package_data=True,
    python_requires='>=3.5',
)