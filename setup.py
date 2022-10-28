import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='simplepylogg3r',
    description='Simple Python Logger package to easily manage custom loggers in Python projects.',
    long_description=long_description,
    author='M4RC0Sx',
    python_requires='>=3.7',
    url='https://github.com/M4RC0Sx/SimplePyLogger',
    project_urls={
        'Source': 'https://github.com/M4RC0Sx/SimplePyLogger',
        'Tracker': 'https://github.com/M4RC0Sx/SimplePyLogger/issues',
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries"
    ],
    packages=setuptools.find_packages(where='.', exclude=('tests', 'tests.*')),
)
