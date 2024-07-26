########################################
#####  IMPORTING MODULES           #####
########################################

#####  INTERNAL IMPORTS
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
        videos: list[Video],
        languages_path: str,
        order_settings: list = ["TITLE", True],
        filter_settings: dict = None,
        tags: list[str] = None
        ) -> None:

        """
        ## Constructor function of Search class

        Parameters
        ----------
        query : str
            Contains the searched value

        videos : list[Video]
            Contains all info about the DataBase

        languages_path : str
            Path to the languages DataBase

        order_settings : list
            Contains what to order with and direction

        filter_settings : dict
            Contains what to filter with

        tags : list[str], optional
            Tags assigned when upload, by default None
        """

        self.videos = videos
        self.query = query
        self.languages_path = languages_path
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

        self.result = search(self.videos, self.query, self.languages_path)
        if self.filter_settings:
            self.result = filter()
        self.result = order(self.order_settings, self.result, self.query, self.tags)
    
    def tags_change(self, tags: list[str]) -> None:
        
        """
        ## Tags change Search function

        Use when user changed the tags of the query. <br>
        Automatically changes the result of the query.
        """

        self.tags = tags
        self.query_server()


    def order_settings_change(self, order_settings: dict) -> None:
        
        """
        ## Order settings change Search function

        Use when user changed order settings. Automatically changes <br>
        the result of the query.
        """
        
        self.order_settings = order_settings
        self.query_server()
        
    def filter_settings_change(self, filter_settings: dict) -> None:
        
        """
        ## Filter settings change Search function

        Use when user changed filter settings. Automatically changes <br>
        the result of the query.
        """
        
        self.filter_settings = filter_settings
        self.query_server()