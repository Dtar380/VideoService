
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

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        VIDEOS: list[dict] = None
    ) -> None:

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
