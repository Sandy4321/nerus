
from setuptools import setup, find_packages


setup(
    name='nerus',
    version='1.4.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nerus-ctl=nerus.ctl.__main__:main'
        ],
    }
)
