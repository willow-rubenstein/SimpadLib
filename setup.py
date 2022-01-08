from setuptools import setup, find_packages
from pathlib import Path


def get_description():
    try:
        return (Path(__file__).parent / "PIP_README.md").read_text()
    except:
        return ""


setup(
    name='simpadlib',
    author='Ashe Muller',
    author_email='contact.notashe@gmail.com',
    version='2.0.0',
    description='A library that allows users to interface with their SimPad devices in real-time',
    long_description=get_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/malevtuber/simpadlib',
    packages=find_packages(),
    ignore_packages=['examples'],
    python_requires='>=3.10',
    install_requires=['pywinusb>=0.4.2'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/malevtuber/simpadlib/issues'
    }
)
