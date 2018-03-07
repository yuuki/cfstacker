from setuptools import setup, find_packages

import stacker

setup(
    name='stacker',
    version=stacker.version,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stacker = stacker.stacker:main',
        ],
    },
    author='yuuki',
    author_email='yuki.tsubo@gmail.com',
    url='https://github.com/yuuki/stacker',
)
