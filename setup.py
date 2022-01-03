import os

from setuptools import find_packages, setup


requirements_file = f"requirements.txt"

with open(requirements_file) as buffer:
    requirements = buffer.read().splitlines()

requirements = list(set(requirements))
requirements_string = "\n  ".join(requirements)

# Collect packages
packages = find_packages(exclude=("tests"))

# Setup the package
setup(
    name="computer",
    version="1.0.0",
    packages=packages,
    python_requires=">=3.10.0",
    install_requires=requirements,
    setup_requires=[],
    ext_modules=[],
    url="https://github.com/JakobHavtorn/computer",
    author="Jakob Havtorn",
    description="Simple simulation of a computer architecture",
    long_description_content_type="text/markdown",
)
