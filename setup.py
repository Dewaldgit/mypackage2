from setuptools import setup, find_packages

setup(
    name='mypackage2',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='DJ',
    description='Second example of a python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Dewaldgit/mypackage2',
    author='<Dewald>',
    author_email='<dewald@hotmail.com>'
)
