from setuptools import find_packages, setup
from os import path

from VideoService import __name__, __author__, __description__, __license__, __version__, __status__

def read(fname):
    with open(path.join(path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()

def main():
    setup(
        name=__name__,
        version=__version__,
        description=__description__,
        package_dir={"": "VideoService"},
        packages=find_packages(where=["VideoService"]),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        url="https://github.com/Dtar380/VideoService",
        author=__author__,
        license=__license__,
        project_urls={
            "Homepage": "https://github.com/Dtar380/VideoService",
            "Documentation": "https://github.com/Dtar380/VideoService/blob/main/README.md",
            "Repository": "https://github.com/Dtar380/VideoService"
        },
        classifiers=[
            "Development Status :: {}".format(__status__),

            "Intended Audience :: Developers",

            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Office/Business",
            "Topic :: Multimedia :: Video",

            "Operating System :: OS Independent",

            "License :: OSI Approved :: {} License".format(__license__),

            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12"
        ],
        install_requires=[read("requirements.txt").splitlines()],
        extra_requires={
            "dev": ["pytest>=8.0.0", "twine>=5.0.0"]
        },
        python_requires=">=3.8"
    )

if __name__ == "__main__":
    main()
