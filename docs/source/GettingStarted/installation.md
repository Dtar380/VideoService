# Installation
This package can be installed in two different ways:
  - [Python Package](#python-package)
  - [Build from source](#build-from-source)

## Python Package
```{note}
This is the best and most common method.
```
As the library is published on [pypi](https://pypi.org/project/VideoService/), it can be installed directly via pip on the terminal.

To install the package you run the command:
<br>
  `pip install VideoService`

If you want to install a custom version instead of the latest you can run:
<br>
  `pip install VideoService==0.2.0`

## Build from source
For building from source you need to follow the next steps:
- First go to release page and select the version. [Here](https://github.com/Dtar380/VideoService/release)
- Then download the `source.zip` file and unzip the file on a custom directory.
- Now make sure you're running a supported python version. (3.8 onwards)
- At last run `python -m pip install -e .[doc]`.

```{note}
You can select extra versions of the package so that it installs extra dependencies, such as -e .[dev]
```

```{warning}
Do not errase the code from the source folder as the python package is running from that source code.
```
