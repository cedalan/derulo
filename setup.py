from setuptools import setup, find_packages

setup(
    name='derulo',
    version='0.1.0',
    description='A utility to parse and display JSON responses from APIs',
    author='Christian Elias Anderssen Dalan',
    author_email='ceadyy@gmail.com',
    url='https://github.com/cedalan/derulo',
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    python_requires='>=3.7',
)
