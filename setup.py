from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="course-recommendation-system",
    version="0.1",
    author="shewani",
    packages=find_packages(),
    install_requires = requirements,
)