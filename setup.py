""" MySQLace - Python interface for MySQL connections.
Copyright (C) 2016  Jordan Yerandi Cortes Guzman

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages
from codecs import open
import os
import re

package_name = 'mySQLace'
here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
os.system("pandoc -f markdown -t rst README.md -o README.rst")
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version number from the __init__.py file in the package
with open(os.path.join(here, package_name, '__init__.py'), encoding='utf-8') as v:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", v.read(), re.M)

    if version_match:
        current_version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    name=package_name,

    version=current_version,

    description="Python interface for MySQL connections",
    long_description=long_description,

    url='https://github.com/jordanncg/mySQLace',

    author='Jordan Yerandi Cortes Guzman',
    author_email='jordancg91@gmail.com',

    license='GPL',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='development mysql connector',

    packages=find_packages(exclude=["contrib", "docs", "tests*"]),

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'mySQLace=mySQLace:main',
        ],
    },
)
