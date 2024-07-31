from setuptools import find_packages, setup
from os import path

from VideoService import __name__, __version__, __description__, __author__, __license__

def read(fname):
    with open(path.join(path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()

def main():
    setup(
        name=VideoService.__name__,
        version=VideoService.__version__,
        description=VideoService.__description__,
        package_dir={"": "VideoService"},
        packages=find_packages(where=["VideoService"]),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        url="",
        author=VideoService.__author__,
        license=VideoService.__license__,
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.12",
            "Operating System :: OS Independent"
        ],
        install_requires=read("requirements.txt").split("\n"),
        extra_requires={
            "dev": ["pytest>=8.0.0", "twine>=5.0.0"]
        },
        python_requires=">=3.12"
    )

if __name__ == "__main__":
    main()
