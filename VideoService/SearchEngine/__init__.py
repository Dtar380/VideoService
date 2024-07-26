########################################
#####  DOCUMENTATION               #####
########################################

"""
SEARCH ENGINE
-------------
Use the custom search engine designed by Dtar380 for the VideoService library. <br>
Multilingual search engine based on percentage of coincidence of a query, with <br>
the ability to filter and order results as user desires. Giving the ability to the user <br>
to change query parameters as fast as possible thanks to the `Search` class <br>
objects implementation.
"""

########################################
#####  IMPORTING MODULES           #####
########################################

#####  INTERNAL IMPORTS
from .search import Search

__all__ = [
    "search_engine.py"
    "search.py"
]