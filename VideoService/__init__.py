########################################
#####  DOCUMENTATION               #####
########################################

"""
VIDEO SERVICE
-------------
### The library you didn't know you needed 🗿

---

This library gives you all you need to create a video<br>
service, Video management, DataBase management,<br>
and an integrated Search Engine.
"""

########################################
#####  IMPORTING MODULES           #####
########################################

#####  INTERNAL IMPORTS
from .__main__ import *
from .SearchEngine.search import Search

__version__ = "0.1.0"
__description__ = "A library to create video services"
__author__ = "Dtar380"
__license__ = "MIT"

__all__ = [
    "__main__.py"
    "videos.py",
    "uploads_manager.py"
    "SearchEngine/search.py"
]