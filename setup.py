# setup.py

from setuptools import setup, find_packages

setup(
    name="webapi",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author="Alphonse SOLOFONDRAIBE",
    author_email="solofondraibedani@gmail.com",
    description="Une bibliothèque pour se connecter aux APIs Web",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alphonse-code/webapi",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
