from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.project_name }}',
    version='0.1',
    description='{{ cookiecutter.project_name }}',
    url='{{ cookiecutter.project_url }}',
    author='{{ cookiecutter.full_name }}',
    author_email='YOUR-EMAIL@ucl.ac.uk',
    license='{{ cookiecutter.open_source_license }}',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    )
)
