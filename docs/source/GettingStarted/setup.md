# Set-Up
In this part of the tutorial you will learn how to set-up your project for using **VideoService** library.
The steps will be:
- [Create directories](#create-directories)
- [Create main.py](#create-mainpy)

## Create directories
First you will need to create the directories required for this library. You can name them as you want, but there are default namings that are better to use.<br>
The structure will be:
- Database/
  - Videos/
  - Thumbnails/
- Uploads/

```{note}
Files will be created on first run, there is no need to create them before start up.
```

## Create main.py
As a convention, we name main.py to the file that we will run when executing our program. This file should be structured as follows:
```python
import VideoService
from VideoService import VideoService

videoservice = VideoService()
```
With this code you will have created your first VideoService database.<br>
All functions and properties of the library are documented onwards.
