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

    def __init__(self,
        query: str,
        videos: list[Video],
        languages_path: str,
        order_settings: list = ["TITLE", True],
        filter_settings: dict = None,
        tags: list[str] = None
        ) -> None:

        self.videos = videos
        self.query = query
        self.languages_path = languages_path
        self.order_settings = order_settings
        self.filter_settings = filter_settings
        self.tags = tags

    def query_server(self):
        self.result = search(self.videos, self.query, self.languages_path)
        if self.filter_settings:
            self.result = filter()
        self.result = order(self.order_settings, self.result, self.query, self.tags)
    
    def tags_change(self, tags: list[str]) -> None:
        self.tags = tags
        self.query_server()

    def filter_settings_change(self, filter_settings: dict) -> None:
        self.filter_settings = filter_settings
        self.query_server()

    def order_settings_change(self, order_settings: dict) -> None:
        self.order_settings = order_settings
        self.query_server()