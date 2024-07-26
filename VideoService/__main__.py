########################################
#####  IMPORTING MODULES           #####
########################################

#####  INTERNAL IMPORTS

# PYTHON BUILT-IN
from typing import List, Union, Dict
from os import path

#####  INTERNAL IMPORTS
from .videos import *
from .uploads_manager import *
from .SearchEngine.search import *
from .__errors__ import *

########################################
#####  CODE                        #####
########################################

#####  CLASS
class VideoService:

    """
    VideoService
    ------------
    Main class of Video Service library (and the only class you'll need 😉)<br>
    This class will manage all the backend of the service, and you will just<br>
    need to call it's methods when required by the server.
    """

    def __init__(self,
        DATABASE: str,
        MINIATURES: str,
        VIDEOS: str,
        UPLOADS: str,
        LANGUAGES: str
        ) -> None:

        """## Constructor function of VideoService class

        Parameters
        ----------
        DATABASE : str
            Path to the DataBase JSON file

        MINIATURES : str
            Path to the Miniatures folder

        VIDEOS : str
            Path to the Videos folder

        UPLOADS : str
            Path to the Uploads folder

        LANGUAGES : str
            Path to the languages DataBase folder

        Raise
        -----
        ValueError 
            If variable was not the expected type

        DataBaseNotFound
            If DataBase JSON was not found

        FolderNotFound
            If folder was not found
        """


        # Check parameters types
        if not isinstance(DATABASE, str):
            raise ValueError("ERROR [VideoService]: DATABASE was expected to be a string")
        if not isinstance(MINIATURES, str):
            raise ValueError("ERROR [VideoService]: MINIATURES was expected to be a string")
        if not isinstance(VIDEOS, str):
            raise ValueError("ERROR [VideoService]: VIDEOS was expected to be a string")
        if not isinstance(UPLOADS, str):
            raise ValueError("ERROR [VideoService]: UPLOADS was expected to be a string")
        if not isinstance(LANGUAGES, str):
            raise ValueError("ERROR [VideoService]: LANGUAGES was expected to be a string")
        
        # Check if folders/files exist and are what they are supposed to be
        if not path.exists(DATABASE) and DATABASE.split(".")[1] != "json":
            raise DataBaseNotFound(f"ERROR [VideoService]: {DATABASE} was not found or is not a JSON")
        if not path.isdir(MINIATURES):
            raise FolderNotFound(f"ERROR [VideoService]: {MINIATURES} was not found")
        if not path.isdir(VIDEOS):
            raise FolderNotFound(f"ERROR [VideoService]: {VIDEOS} was not found")
        if not path.isdir(UPLOADS):
            raise FolderNotFound(f"ERROR [VideoService]: {UPLOADS} was not found")
        if not path.isdir(LANGUAGES):
            raise FolderNotFound(f"ERROR [VideoService]: {LANGUAGES} was not found")

        self.DATABASE = DATABASE
        self.VIDEOS = VIDEOS
        self.MINIATURES = MINIATURES
        self.UPLOADS = UPLOADS
        self.LANGUAGES = LANGUAGES

        self.videos = self.__init_database()
        self.uploads = self.__init_uploads_manager()

    # PRIVATE METHOD TO INITIALISE THE DATABASE
    def __init_database(self) -> Videos:
        return Videos(
            DATABASE = self.DATABASE,
            MINIATURES = self.MINIATURES,
            VIDEOS = self.VIDEOS
        )

    # PRIVATE METHOD TO INITIALISES THE UPLOADS MANAGER
    def __init_uploads_manager(self) -> UploadManager:
        return UploadManager(
            UPLOADS = self.UPLOADS,
            MINIATURES = self.MINIATURES,
            VIDEOS = self.VIDEOS
        )

    def upload(self, 
        TITLE: str, 
        VIDEO_FILENAME: str, 
        MINIATURE_FILENAME: str, 
        DESCRIPTION: str = None, 
        TAGS: List[str] = None
        ) -> None:

        """
        ## Method used to upload files to the DataBase

        Parameters
        ----------
        TITLE : str
            Title provided for the video

        VIDEO_FILENAME : str
            File name of the video

        MINIATURE_FILENAME : str, optional
            File name of the miniature for the video , by default None

        DESCRIPTION : str, optional
            Description for the video, by default None

        TAGS : list[str], optional
            Tags for the video, by default None

        Raise
        -----
        ValueError
            If variable was not the expected type

        FolderNotFound
            If folder was not found
        """

        # Check parameters types
        if not isinstance(TITLE, str):
            raise ValueError("ERROR [VideoService]: TITLE was expected to be a str")
        if not isinstance(VIDEO_FILENAME, str):
            raise ValueError("ERROR [VideoService]: VIDEO_FILENAME was expected to be a str")
        if not isinstance(MINIATURE_FILENAME, str):
            raise ValueError("ERROR [VideoService]: MINIATURE_FILENAME was expected to be a str")
        if DESCRIPTION and not isinstance(DESCRIPTION, str):
            raise ValueError("ERROR [VideoService]: DESCRIPTION was expected to be a str")
        if TAGS and not check_tags(TAGS):
            raise ValueError("ERROR [VideoService]: TAGS was expected to be a list[str]")

        # Check that files exist
        if not path.isfile(path.join(self.UPLOADS, VIDEO_FILENAME)):
            raise FileNotFoundError(f"ERROR [VideoService]: {VIDEO_FILENAME} was not found")
        if not path.isfile(path.join(self.UPLOADS, MINIATURE_FILENAME)):
            raise FileNotFoundError(f"ERROR [VideoService]: {MINIATURE_FILENAME} was not found")

        self.videos = self.uploads.upload(
            videos = self.videos,
            TITLE = TITLE,
            VIDEO_FILENAME = VIDEO_FILENAME,
            MINIATURE_FILENAME = MINIATURE_FILENAME,
            DESCRIPTION = DESCRIPTION,
            TAGS = TAGS
        )

    def save_videos(self):


        """
        ## Method used to save videos to the DataBase

        Save_videos transforms the `videos` list to a dictionary to then save it<br>
        to the DataBase JSON file.
        Automatically performed by the server when a new Video is uploaded.
        """

        self.videos.save_videos()

    def delete_video(self,
        VIDEO_ID: int = None,
        VIDEO_FILENAME: str = None
        ) -> None:

        """
        ## Method used to delete videos from the DataBase

        Delete_video deletes a video from the `videos` list given specific parameters.

        Parameters
        ----------
        VIDEO_ID : int, optional
            Index that leads to the video on the `videos` list, by default None

        VIDEO_FILENAME : str, optional
            Filename of the video, by default None

        **Requires only one of both parameter**

        Raise
        -----
        ValueError
            If variable was not the expected type
        """

        # Check parameters type
        if VIDEO_ID and not isinstance(VIDEO_ID, int):
            raise ValueError("ERROR [VideoService]: VIDEO_ID was expected to be a str")
        if VIDEO_FILENAME and not isinstance(VIDEO_FILENAME, str):
            raise ValueError("ERROR [VideoService]: VIDEO_ID was expected to be a str")
        
        self.videos.delete_video(
            VIDEO_ID=VIDEO_ID,
            VIDEO_FILENAME=VIDEO_FILENAME
        )

    def query(self,
        query: str,
        order_settings: List[ Union[ str, bool]] = None,
        filter_settings: Dict[str, Dict[str, Union[List[Union[str, int]], bool]]] = None,
        tags: List[str] = None
        ) -> Search:

        """
        ## Method used to perform a query
        
        Parameters
        ----------
        query : str
            Contains the searched value

        order_settings : list[str | bool]
            Contains what to order with and direction

        filter_settings : dict[str, dict[str, List[str | int] | bool]]
            Contains what to filter with

        tags : list[str], optional
            Tags assigned when upload, by default None

        Returns
        -------
        Search : Search
            Contains all info about the query

        Raise
        -----
            **ValueError**<br>
            **WrongOrderStructure**<br>
            **WrongFilterStructure**<br>
            **WrongTagsStructure**<br>
            If variable was not the expected type
        """

        # Check parameters type
        if not isinstance(query, str):
            raise ValueError("ERROR [VideoService]: query was expected to be a str")
        if order_settings and check_order_settings(order_settings):
            raise WrongOrderStructure("ERROR [VideoService]: order_settings was given a wrong structure, see documentation")
        if filter_settings and check_filter_settings(filter_settings):
            raise WrongFilterStructure("ERROR [VideoService]: filter_settings was given a wrong structure, see documentation")
        if tags and check_tags(tags):
            raise WrongTagsStructure("ERROR [VideoService]: tags was given a wrong structure, see documentation")

        return Search(
            query = query,
            videos = self.videos,
            LANGUAGES = self.LANGUAGES,
            order_settings = order_settings,
            filter_settings = filter_settings,
            tags = tags
        )