########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS

# PYTHON BUILT-IN
from typing import Union, Dict, List

#####  INTERNAL IMPORTS
from ..__errors__ import *
from .search_engine import search, order, filter
from ..videos import Video

########################################
#####  CODE                        #####
########################################

#####  CLASS
class Search:

    """
    Search
    ------
    A Search object is created when ever a search is performed by <br>
    a user, and it contains all info about the query.
    """

    def __init__(self,
        query: str,
        videos: List[Video],
        LANGUAGES: str,
        order_settings: list = ["TITLE", True],
        filter_settings: Dict[str, Dict[str, Union[List[Union[str, int]], bool]]] = {
            "_filter_by_date": {
                "filter": [],
                "active": False
                },
            "_filter_by_length": {
                "filter": [],
                "active": False
                },
            "_filter_by_tags": {
                "filter": [],
                "active": False
                }
        },
        tags: List[str] = None
        ) -> None:

        """
        ## Constructor function of Search class

        Parameters
        ----------
        query : str
            Contains the searched value

        videos : list[Video]
            Contains all info about the DataBase

        LANGUAGES : str
            Path to the languages DataBase

        order_settings : list[str | bool]
            Contains what to order with and direction <br>
            Default, by Title coincidence descendant

        filter_settings : dict[str, dict[str, List[str | int] | bool]], optional
            Contains what to filter with <br>
            Default, deactivated every filter

        tags : list[str], optional
            Tags assigned when upload, by default None
        """

        self.videos = videos
        self.query = query
        self.LANGUAGES = LANGUAGES
        self.order_settings = order_settings
        self.filter_settings = filter_settings
        self.tags = tags

        self.query_server

    def query_server(self) -> None:

        """
        ## Query server function

        Use when want to perform a query to the server. <br>
        Sets the class variable `result` to the result of <br>
        the query.
        """

        self.result = search(
            videos = self.videos,
            query = self.query,
            LANGUAGES = self.LANGUAGES
        )

        if self.filter_settings:
            self.result = filter(
                videos = self.result,
                filter_settings = self.filter_settings
            )

        self.result = order(
            videos = self.result,
            order_settings = self.order_settings,
            title = self.query,
            tags = self.tags
        )
    
    def tags_change(self, tags: List[str]) -> None:
        
        """
        ## Tags change Search function

        Use when user changed the tags of the query. <br>
        Automatically changes the result of the query.

        
        Parameters
        ----------
        tags : list[str]
            Tags searched for the video

        Raise
        -----
        WrongTagsStructure
            If variable was not the expected type
        """

        if not check_tags(tags):
            raise WrongTagsStructure("ERROR [VideoService]: tags was given a wrong structure, see documentation")

        self.tags = tags
        self.query_server()


    def order_settings_change(self, order_settings: List[ Union[ str, bool ] ] ) -> None:
        
        """
        ## Order settings change Search function

        Use when user changed order settings. Automatically changes <br>
        the result of the query.

        Parameters
        ----------
        order_settings : list[str | bool]
            List containing the parameter to use and way to order<br>
            If Second value True descendant order if False ascendant

        Raise
        -----
        WrongOrderStructure
            If variable was not the expected type
        """

        if not check_order_settings(order_settings):
            raise WrongOrderStructure("ERROR [VideoService]: order_settings was given a wrong structure, see documentation")

        self.order_settings = order_settings
        self.query_server()
        
    def filter_settings_change(self,
        filter_settings: Dict[str, Dict[str, Union[List[Union[str, int]], bool]]]
        ) -> None:
        
        """
        ## Filter settings change Search function

        Use when user changed filter settings. Automatically changes <br>
        the result of the query.

        Parameters
        ----------
        filter_settings : dict[str, dict[str, List[str | int] | bool]]
            Dict containing the parameters to use

        filter_setting structure:

        .. code-block:: python
            {
            "_filter_by_date": {
                "filter": List[str],
                "active": True | False
                },
            "_filter_by_length": {
                "filter": List[int],
                "active": True | False
                },
            "_filter_by_tags": {
                "filter": List[str],
                "active": True | False
                }
            }

        Raise
        -----
        WrongFilterStructure
            If variable was not the expected type
        """
        
        if not check_filter_settings(filter_settings):
            raise WrongFilterStructure("ERROR [VideoService]: filter_settings was given a wrong structure, see documentation")

        self.filter_settings = filter_settings
        self.query_server()