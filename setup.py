from setuptools import setup, find_packages

setup(
    name='django-toolbar-statsd',
    version='0.1',
    description='',
    long_description='',
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    packages=['toolbar_statsd'],
    url='',
    package_data = {'toolbar_statsd': ['templates/toolbar_statsd/*.html']},
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Django'
        ],
    )
