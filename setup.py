from setuptools import setup

setup(
    name='geolucidate',
    version='0.4',
    description='Parse free-form geographic coordinates in text, and automatically generate links and metadata.',
    author='Kurt Raschke',
    author_email='kurt@kurtraschke.com',
    url='http://github.com/kurtraschke/geolucidate',
    license = "MIT",
    
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Scientific/Engineering :: GIS"
        ],

    packages=[
        "geolucidate",
        "geolucidate.links",
        "geolucidate.tests",
    ],
    test_suite='nose.collector',
    tests_require=['nose'])
