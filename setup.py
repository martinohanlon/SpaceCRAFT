from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="spacecraft",
    version="0.2.0",
    description="SpaceCRAFT - A module for rendering astro pi data in Minecraft",
    long_description=long_description,
    url="https://github.com/martinohanlon/SpaceCRAFT",
    author="Martin O'Hanlon",
    author_email="martin@ohanlonweb.com",
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
        "Topic :: Education",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        
    ],
    keywords=[
        "raspberrypi",
        "astro pi",
        "astro pi hat",
        "sense hat",
        "minecraft",
        "spacecraft",
    ],
    packages=find_packages(exclude=["poc", "scripts"]),
    install_requires=["sense-hat"],
)
