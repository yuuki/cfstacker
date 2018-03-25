from setuptools import setup, find_packages

import cfstacker

setup(
    name='cfstacker',
    version=cfstacker.version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cfstacker = cfstacker.cfstacker:main',
        ],
    },
    author='yuuki',
    author_email='yuki.tsubo@gmail.com',
    url='https://github.com/yuuki/cfstacker',
)
