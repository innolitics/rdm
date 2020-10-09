"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

description = 'Regulatory Documentation Manager'

setup(
    name='rdm',
    version='0.9.2',
    description=description,
    long_description=description,
    url='https://github.com/innolitics/rdm',
    author='Innolitics, LLC',
    author_email='info@innolitics.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='regulatory documentation medical iec62304 iec82304 iso14971',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['jinja2>=2.7', 'pyyaml', 'gitpython', 'jsonschema'],
    extras_require={
        'svg': ['svglib', 'reportlab'],
        'github': ['pygithub'],
        'dev': ['check-manifest', 'sphinx', 'sphinx-autobuild', 'mock'],
        'test': ['coverage'],
    },
    package_data={'rdm': [
        'base/*',
        'checklists/*',
        'init_files/.gitignore',
        'init_files/*',
        'init_files/data/*',
        'init_files/images/*',
        'init_files/images/uimockups/*',
        'init_files/documents/*',
        'hook_files/*'
    ]},
    data_files=[],
    entry_points={
        'console_scripts': [
            'rdm = rdm.main:main'
        ]
    },
)
