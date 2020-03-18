# setup.py - setup script for the 'hg-convert-prcs' package
# Copyright (C) 2019-2020 Kaz Nishimura
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""setup script for the hg-convert-prcs package
"""

from os import path
from setuptools import setup, find_packages

# Package version.
PACKAGE_VERSION = "1a1"

def long_description():
    """return the long description from the 'README.md' file
    """
    cwd = path.abspath(path.dirname(__file__))
    with open(path.join(cwd, "README.md"), encoding="UTF-8") as file:
        # To ignore lines until a level-1 ATX header is found.
        while True:
            line = file.readline()
            if line.startswith("# "):
                break
        return line + file.read()

if __name__ == "__main__":
    setup(
        name="hg-convert-prcs",
        version=PACKAGE_VERSION,
        description="PRCS source for the Mercurial convert extension.",
        url="https://vx68k.bitbucket.io/hg-convert-prcs/",
        author="Kaz Nishimura",
        author_email="kazssym@vx68k.org",
        long_description=long_description(),
        long_description_content_type="text/markdown",
        classifiers=[
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Programming Language :: Python :: 3",
        ],
        python_requires=">= 3.4",
        install_requires=[
            "mercurial >= 4.7",
            "prcslib >= 1.0b2"
        ],

        packages=find_packages(exclude=["testsuite", "testsuite.*"]),
        py_modules=["hgext3rd/convert/prcs"],
        test_suite="testsuite",
    )
