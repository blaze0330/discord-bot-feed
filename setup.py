import setuptools

from discord_ext.about import (
    __title__,
    __version__,
    __description__,
    __package_name__,
    __author__,
    __email__,
    __license__,
    __github__
)

with open("README.md", "r") as fh:
    long_description = fh.read()


print("Installing {} v{}".format(__title__, __version__))
print(__package_name__)


setuptools.setup(
    name=__package_name__,
    version=__version__,
    author=__author__,
    author_email=__email__,
    description=__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=__github__,
    install_requires=[
        'requests==2.28.1',
        'discord-webhook==1.0.0',
        'colorama==0.4.6'
        ],
    keywords="rssfeed, rssfeedcli, rssfeed-cli",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.1",
    # entry_points={
    #     "console_scripts": ["movens = movens.cli:main"],
    # },
)
