from setuptools import setup, find_packages


setup(
    name='sublime_core_tests',
    version='1.0.0',
    description='Modest test suite to verify Sublime Text functionality',
    long_description=open('README.rst').read(),
    keywords=[
        'test',
        'sublime',
        'sublime text'
    ],
    author='Todd Wolfson',
    author_email='todd@twolfson.com',
    url='https://github.com/twolfson/sublime-core-tests',
    download_url='https://github.com/twolfson/sublime-core-tests/archive/master.zip',
    packages=find_packages(),
    license='UNLICENSE',
    install_requires=open('requirements.txt').readlines(),
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ]
)
