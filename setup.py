from setuptools import setup, find_packages
from opensee.__version__ import __version__


setup(
    name="opensee",
    author="James Campbell",
    author_email="james@jamescampbell.us",
    version=__version__,
    license="MIT",
    description="get info from opensea",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["opensee"],
    py_modules=["opensee"],
    keywords=["cryptocrap", "nft", "data-analysis", "bi",
              "business-inteligence"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["requests-html", "beautifulsoup4"],
    entry_points={"console_scripts": ["opensee = opensee.opensee:main"]},
    url="https://github.com/jamesacampbell/opensee",
    download_url="https://github.com/jamesacampbell/opensee/archive/{}.tar.gz".format(
        __version__
    ),
)
