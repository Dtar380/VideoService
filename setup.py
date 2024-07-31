from setuptools import find_packages, setup
from os import path

def read(fname):
    with open(path.join(path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()

def main():
    setup(
        name="VideoService",
        version="0.1.1",
        description="A library to create video services",
        package_dir={"": "VideoService"},
        packages=find_packages(where=["VideoService"]),
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        url="",
        author="Dtar380",
        license="MIT",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3.12",
            "Operating System :: OS Independent"
        ],
        install_requires=[
            "opencv-python==4.10.0.84",
            "lingua-language-detector==2.0.2"
        ],
        extra_requires={
            "dev": ["pytest>=8.0.0", "twine>=5.0.0"]
        },
        python_requires=">=3.12"
    )

if __name__ == "__main__":
    main()
