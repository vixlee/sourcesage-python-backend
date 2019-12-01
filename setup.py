#!/usr/bin/env python

from setuptools import setup, find_packages

# Based on http://www.dabeaz.com/generators/ and http://cburgmer.posterous.com/pip-requirementstxt-and-setuppy  # noqa
import re
import os
import sys

PY_VER_STR = "py%d%d" % sys.version_info[:2]


def gen_find_applicable_requirements_filenames(base_filename):
    """
    Generator that yields the passed base requirements filename, along with its
    version specific requirements filename (if exists)
    """
    yield base_filename

    base, ext = os.path.splitext(base_filename)
    version_specific_filename = "%s.%s%s" % (base, PY_VER_STR, ext)
    if os.path.exists(version_specific_filename):
        yield version_specific_filename


def gen_open_files(filenames):
    """
    Generator that takes an iterable containing filenames as input and yields a
    sequence of file objects that have been suitably open
    """
    for name in filenames:
        yield open(name)


def gen_cat(sources):
    """
    Generator that concatenates multiple generators into a single sequence
    """
    for s in sources:
        for item in s:
            yield item


def gen_lines_from_requirements(base_filename):
    """
    Generator that finds all applicable requirements filenames and yields their
    contents, line at a time
    """
    filenames = gen_find_applicable_requirements_filenames(base_filename)
    files = gen_open_files(filenames)
    lines = gen_cat(files)
    return lines


def parse_requirements(base_filename):
    """
    Finds all applicable requirements filenames, parse them and return the
    requirements
    """
    requirements = []
    for line in gen_lines_from_requirements(base_filename):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'\s*-f\s+', line):
            pass
        else:
            requirements.append(line)

    return requirements


with open("user_api/version.py") as f:
    exec(f.read())

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(name='user_api',
      version=__version__,  # noqa
      description='Le Hung Vi - SourceSage Python Techincal test',
      long_description=long_description,
      author='VixLee',
      author_email='lehungvi.cntt@gmail.com',
      url='https://github.com/vixlee',
      scripts=[
          "bin/user_api",
      ],
      packages=find_packages(),
      install_requires=parse_requirements('requirement.txt'),
      entry_points={
          'console_scripts': [
              'user_api = user_api.app:main',
          ]
      },
      )

