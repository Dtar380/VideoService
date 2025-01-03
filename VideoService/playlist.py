
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

# *** Python modules *** #
from .video import Video
from .__errors__ import *

#################################################*
##### ***  CODE  ***    #########################*
#################################################*

### *** PLAYLIST CLASS *** ###
class Playlist:

    """
    Playlist
    ========
    A class to represent a playlist object.
    """

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        VIDEOS: list[dict] = None
    ) -> None:

        """
        Class Constructor
        =================

        Parameters
        ----------
        TITLE : str
            The title of the playlist.

        OWNER : str
            The owner of the playlist.

        VISIBILITY : str
            The visibility of the playlist.

        DESCRIPTION : str, optional
            The description of the playlist.

        TAGS : list[str], optional
            The tags of the playlist.

        VIDEOS : list[dict], optional
            The videos of the playlist.
        """

        # Set arguments as class attributes
        self.TITLE = TITLE
        self.OWNER = OWNER
        self.VISIBILITY = VISIBILITY
        # Set optional arguments as class attributes
        self.DESCRIPTION = DESCRIPTION or ""
        self.TAGS = TAGS or [""]
        self.VIDEOS = VIDEOS or []


    ## *** CLASS PROPERTIES *** ##
    # *** PLAYLIST JSON *** #
    @property
    def playlist(self) -> dict:

        """
        Playlist JSON
        =============
        Get a JSON object representing the playlist.

        Returns
        -------
        dict
            A JSON object representing the playlist.
        """

        # Create a playlist JSON object
        playlist_json = {
            "TITLE": self.TITLE,
            "OWNER": self.OWNER,
            "VISIBILITY": self.VISIBILITY,
            "DESCRIPTION": self.DESCRIPTION,
            "TAGS": self.TAGS,
            "VIDEOS": self.VIDEOS
        }

        return playlist_json

    ## *** CLASS METHODS *** ##
    # *** STRING REPRESENTATION *** #
    def __str__(self) -> str:
        return str(self.playlist)

    # *** ADD VIDEO *** #
    def add_video(self, video_: Video) -> None:

        """
        Add Video
        =========
        Add a video to the playlist.

        Parameters
        ----------
        video_ : Video
            The video to add to the playlist.
        """

        try:
            # Check if the video already exists in the playlist
            if self.__video_exists(video_):
                raise AlreadyExistsError("ERROR [Playlist]: The video already exists in the playlist")
            else:
                # Add the video to the playlist
                self.VIDEOS.append(video_.video)

        except Exception as error:
            # Parse error and print message
            print(error_parser(error))

    # *** REMOVE VIDEO *** #
    def remove_video(self, video_: Video) -> None:

        """
        Remove Video
        ============
        Remove a video from the playlist.

        Parameters
        ----------
        video_ : Video
            The video to remove from the playlist.
        """

        try:
            # Check if the video exists in the playlist
            if self.__video_exists(video_):
                # Remove the video from the playlist
                self.VIDEOS.remove(video_.video)
            else:
                raise NotFoundError("ERROR [Playlist]: The video does not exist in the playlist")

        except Exception as error:
            # Parse error and print message
            print(error_parser(error))

    ## *** PRIVATE METHODS *** ##
    # *** VIDEO EXISTS *** #
    def __video_exists(self, video_: Video) -> bool:
        # Get the videos from the playlist
        videos = [video for video in self.VIDEOS]
        # Check if the video exists in the playlist
        return video_.video in videos
