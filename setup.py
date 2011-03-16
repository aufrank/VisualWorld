from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
    'visionegg',
    'pyaudio'
]

dependency_links = [
    "https://github.com/cedrus-opensource/pyxid",
    # "https://www.sr-support.com/forums/showthread.php?t=14"
]

setup(name='visualworld',
    version=version,
    description="Visual world experiments with eye tracking, mouse tracking, mouse and keyboard responses, and audio input and output",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='',
    author='Austin F. Frank',
    author_email='aufrank@haskins.yale.edu',
    url='',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['visualworld=visualworld:main']
    }
)
