import os
from setuptools import setup


def get_packages(package):
    return [dirpath for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


setup(
    name='django-admin-rangefilter',
    version='0.1',
    description="Custom rangefilter",
    url='https://github.com/takitakis/django-admin-rangefilter',
    author='Takeaki Kawai',
    author_email='taki.kwi@gmail.com',
    license='MIT',
    keywords='rangefilter',
    packages=get_packages('rangefilter'),
    package_data=get_package_data('rangefilter'),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)