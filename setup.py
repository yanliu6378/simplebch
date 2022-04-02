from setuptools import setup, Extension

module = Extension("simplebch", sources=["simplebch.c"])

setup(
    name="simplebch",
    version="0.1.0",
    description="A simple BCH encoding and decoding library",
    author="Yan Liu",
    author_email="uh60mh47ah6@proton.me",
    url="https://github.com/uh60mh47ah6/simplebch",
    ext_modules=[module],
    python_requires='>=3.8',
)
