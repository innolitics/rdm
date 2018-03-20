"""
A setuptools based setup module.
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

description = 'Regulatory Documentation Manager'

setup(
    name='rdm',
    version='0.1.0',
    description=description,
    long_description=description,
    url='https://github.com/innolitics/rdm',
    author='Innolitics, LLC',
    author_email='info@innolitics.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='regulatory documentation medical iec62304',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['jinja2>=2.7', 'pyyaml'],
    extras_require={
        'dev': ['check-manifest', 'sphinx', 'sphinx-autobuild', 'mock'],
        'test': ['coverage'],
    },
    package_data={'rdm': ['init/*', 'init/data/*', 'init/templates/*']},
    data_files=[],
    entry_points={
        'console_scripts': [
            'rdm = rdm.main:main'
        ]
    },
)
