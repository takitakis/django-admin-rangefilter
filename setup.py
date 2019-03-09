from setuptools import setup


setup(
    name='django-admin-rangefilter',
    version='0.1',
    description="Custom rangefilter",
    url='https://github.com/takitakis/django-admin-rangefilter',
    author='Takeaki Kawai',
    author_email='taki.kwi@gmail.com',
    license='MIT',
    keywords='rangefilter',
    packages=[
        "rangefilter",
    ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)