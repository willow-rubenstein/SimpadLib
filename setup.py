from setuptools import setup
from pathlib import Path

def getDescription():
    try:
        return (Path(__file__).parent / "PIP_README.md").read_text()
    except:
        return ""

setup(
    name='simpadlib',
    author='Ashe Muller',
    author_email='contact.notashe@gmail.com',
    version='1.0.2',
    description='A library that allows users to custom-configure their SimPad real-time',
    long_description=getDescription(),
    long_description_content_type='text/markdown',
    url='https://github.com/malevtuber/simpadlib',
    package_dir={'': 'src'},
    python_requires='>=3.10',
    install_requires=['pywinusb>=0.4.2'],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/malevtuber/simpadlib/issues'
    }
)