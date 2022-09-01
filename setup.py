from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Easily get kivy widget instances to use them'
LONG_DESCRIPTION = """On the "view" side, if you're working with multiple kivy widget classes and you're sending 
information that has a "parent-child" relationship between those classes. After a while the codes become 
incomprehensible. "Kivy Widget Finder" extracts the tree of all widgets from any instance you provide and brings you 
the instance of the class you want to access."""

# Setting up
setup(
    name="kivy-widget-finder-que",
    version=VERSION,
    author="Que (Bugra Muaz Mujde)",
    license="MIT License (MIT)",
    requires="Python >=3.7",
    author_email="<mujdebugra@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    requires_python=">=3.0",
    packages=find_packages(),
    install_requires=['kivy'],
    keywords=['python', 'kivy', 'widget', 'finder', 'parent-child', 'instance'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
