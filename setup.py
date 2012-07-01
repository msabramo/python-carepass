import sys

extra = {}
if sys.version_info >= (3, 0):
    extra.update(use_2to3=True)

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from distutils.core import setup, find_packages, Command

import multiprocessing

author = "Marc Abramowitz"
email = "marc@marc-abramowitz.com"

setup(name='python-carepass',
      version='0.0.0',
      description='',
      long_description='',
      data_files=[('', ['README.rst'])],
      classifiers=[
            'License :: OSI Approved :: BSD License',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.4',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
          ],
      author=author,
      author_email=email,
      url='http://github.com/msabramo/anyserializer',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      platforms=["any"],
      install_requires=['requests'],
      tests_require=['nose'],
      test_suite = 'nose.collector',
      **extra
)
