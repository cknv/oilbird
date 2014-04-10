from setuptools import setup
import oilbird

setup(
    name='oilbird',
    version=oilbird.version,
    author='Esben Sonne',
    author_email='esbensonne@gmail.com',
    license='MIT',
    url='https://github.com/cknv/oilbird',
    install_requires=[
        'requests>=1.0',
        'args==0.1.0',
        'clint==0.3.6',
    ],
    entry_points={
        'console_scripts': [
            'oilbird = oilbird.cli:main',
        ]
    }
)
