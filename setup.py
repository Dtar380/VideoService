from setuptools import find_packages, setup
from os import path

def read(fname):
    with open(path.join(path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()

def main():
    setup(
        name="VideoService",
        version="0.1.2",
        description="A library to create video services",
        package_dir={"": "VideoService"},
        packages=find_packages(where=["VideoService"]),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        url="https://github.com/Dtar380/VideoService",
        author="Dtar380",
        license="MIT",
        project_urls={
            "Homepage": "https://github.com/Dtar380/VideoService",
            "Documentation": "https://github.com/Dtar380/VideoService/blob/main/README.md",
            "Repository": "https://github.com/Dtar380/VideoService"
        },
        classifiers=[
            "Development Status :: 4 - Beta",

            "Intended Audience :: Developers",

            "Topic :: Database :: Database Engines/Servers",
            "Topic :: Office/Business",
            "Topic :: Multimedia :: Video",

            "Operating System :: OS Independent",

            "License :: OSI Approved :: MIT License",

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
