import io
import os
import sys

from setuptools import setup

if sys.version_info < (3, 6):
    sys.exit('Sorry, Python < 3.6.0 is not supported')

DESCRIPTION = 'Images Generator for bouncing objects movie'
here = os.path.abspath(os.path.dirname(__file__))
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# load __version__
exec(open(os.path.join(here, 'bouncing_objects_generator', '_version.py')).read())

setup(
    name='bouncing_objects_generator',
    version=__version__,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kazuhiro Serizawa',
    author_email='nserihiro@gmail.com',
    url='https://github.com/serihiro/bouncing_objects_generator',
    license='MIT',
    packages=['bouncing_objects_generator'],
    install_requires=['numpy>=1.15', 'pillow>=5.0'],
    entry_points={
        'console_scripts': ['bouncing_objects_generator=bouncing_objects_generator.cli:main']
    }
)
