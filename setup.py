from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name='mltrain',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'tensorflow'
    ],
    long_description=description,
    long_description_content_type='text/markdown'
)
