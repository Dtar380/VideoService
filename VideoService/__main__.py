
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

# *** Python modules *** #
import os

# *** Internal modules *** #
from .database import Database
from .files_manager import FileManager
from .video import Video
from .playlist import Playlist
from .__errors__ import *

#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

### *** VIDEO SERVICE CLASS *** ###
class VideoService:

    """
    VideoService
    ============
    Main class of Video Service library.

    This class will manage all the backend of the service, and you will just
    need to call it's methods when required by the server.
    """

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        DATABASE: str = ".\\Database",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS",
        UPLOADS: str = ".\\Uploads"
    ) -> None:

        """
        Class Constructor
        =================

        Parameters
        ----------
        DATABASE : str, optional
            Path to the database file.

        VIDEOS : str, optional
            Path to the videos folder.

        THUMBNAILS : str, optional
            Path to the thumbnails folder.

        UPLOADS : str, optional
            Path to the uploads folder.

        Raises
        ------
        TypeError
            If the paths are not strings.

        NotFoundError
            If the paths do not exist.
        """

        # Check if arguments are valid
        args_handling(
            init=True,
            DATABASE=DATABASE,
            VIDEOS=VIDEOS,
            THUMBNAILS=THUMBNAILS,
            UPLOADS=UPLOADS
        )

        # Set arguments as class attributes
        self.DB_PATH = DATABASE
        self.VIDEOS_PATH = VIDEOS
        self.THUMBNAILS_PATH = THUMBNAILS
        self.UPLOADS_PATH = UPLOADS

        # Create instances of Database and FileManager
        self.database = Database(
            DATABASE=DATABASE,
            VIDEOS=VIDEOS,
            THUMBNAILS=THUMBNAILS
        )
        self.file_manager = FileManager(
            VIDEOS=VIDEOS,
            THUMBNAILS=THUMBNAILS,
            UPLOADS=UPLOADS
        )

    ## *** CLASS METHODS *** ##
    # *** UPLOAD VIDEO TO SERVER AND DATABASE *** #
    def upload(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        OWNER: str,
        VISIBILITY: str,
        THUMBNAIL_FILENAME: str = None,
        DESCRIPTION: str = None,
        TAGS: list[str] = None
    ) -> dict:

        """
        Upload
        ======
        Function to upload a video to the server and database.

        Parameters
        ----------
        TITLE : str
            Title of the video.

        VIDEO_FILENAME : str
            Filename of the video.

        OWNER : str
            Owner of the video.

        VISIBILITY : str
            Visibility of the video.

        THUMBNAIL_FILENAME : str, optional
            Filename of the thumbnail.

        DESCRIPTION : str, optional
            Description of the video.

        TAGS : list[str], optional
            Tags of the video.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        try:
            # Set optional arguments as empty strings or lists
            THUMBNAIL_FILENAME = THUMBNAIL_FILENAME or ""
            DESCRIPTION = DESCRIPTION or ""
            TAGS = TAGS or [""]

            # Check if arguments are valid
            args_handling(
                init=False,
                TITLE=TITLE,
                VIDEO_FILENAME=VIDEO_FILENAME,
                OWNER=OWNER,
                VISIBILITY=VISIBILITY,
                THUMBNAIL_FILENAME=THUMBNAIL_FILENAME,
                DESCRIPTION=DESCRIPTION,
                TAGS=TAGS
            )

            # Check if files exist
            if not os.path.isfile(os.path.join(self.UPLOADS_PATH, VIDEO_FILENAME)):
                raise FileNotFoundError(f"ERROR [VideoService]: The file '{VIDEO_FILENAME}' does not exist")
            if THUMBNAIL_FILENAME and not os.path.isfile(os.path.join(self.UPLOADS_PATH, THUMBNAIL_FILENAME)):
                raise FileNotFoundError(f"ERROR [VideoService]: The file '{THUMBNAIL_FILENAME}' does not exist")

        except Exception as error:
            # Print error and return message
            error = error_parser(error)
            print(error)
            return {
                "message": error,
                "status": 500
            }

        # Upload the files to the server and get the result
        video_ = self.file_manager.upload_file(
            TITLE=TITLE,
            VIDEO_FILENAME=VIDEO_FILENAME,
            OWNER=OWNER,
            VISIBILITY=VISIBILITY,
            THUMBNAIL_FILENAME=THUMBNAIL_FILENAME,
            DESCRIPTION=DESCRIPTION,
            TAGS=TAGS
        )

        # Check if 'video_' is a dictionary
        if isinstance(video_, dict):
            return video_

        # Return the result of 'add_video' method
        return self.database.add_video(video_=video_)

    # *** CREATE PLAYLIST *** #
    def create_playlist(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
    ) -> dict:

        """
        Create Playlist
        ===============
        Function to create a playlist.

        Parameters
        ----------
        TITLE : str
            Title of the playlist.

        OWNER : str
            Owner of the playlist.

        VISIBILITY : str
            Visibility of the playlist.

        DESCRIPTION : str, optional
            Description of the playlist.

        TAGS : list[str], optional
            Tags of the playlist.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        try:
            # Set optional arguments as empty strings or lists
            DESCRIPTION = DESCRIPTION or ""
            TAGS = TAGS or [""]

            # Check if arguments are valid
            args_handling(
                init=False,
                TITLE=TITLE,
                OWNER=OWNER,
                VISIBILITY=VISIBILITY,
                DESCRIPTION=DESCRIPTION,
                TAGS=TAGS
            )

        except Exception as error:
            # Print error and return message
            error = error_parser(error)
            print(error)
            return {
                "message": error,
                "status": 500
            }

        # Return the result of 'add_playlist' method
        return self.database.add_playlist(
            # Pass the result of 'create_playlist' method as 'playlist_'
            playlist_ = Playlist(
                TITLE=TITLE,
                OWNER=OWNER,
                VISIBILITY=VISIBILITY,
                DESCRIPTION=DESCRIPTION,
                TAGS=TAGS
            )
        )

    # *** SAVE VIDEOS *** #
    def save_videos(self) -> dict:

        """
        Save Videos
        ===========
        Function to save videos to the database.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'save_videos' method
        return self.database.save_videos()

    # *** SAVE PLAYLISTS *** #
    def save_playlists(self) -> dict:

        """
        Save Playlists
        ==============
        Function to save playlists to the database.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'save_playlists' method
        return self.database.save_playlists()

    # *** DELETE VIDEO *** #
    def delete_video(self, video_: Video) -> dict:

        """
        Delete Video
        ============
        Function to delete a video.

        Parameters
        ----------
        video_ : Video
            Video to delete.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'delete_video' method
        return self.database.delete_video(video_=video_)

    # *** DELETE PLAYLIST *** #
    def delete_playlist(self, playlist_: Playlist) -> dict:

        """
        Delete Playlist
        ===============
        Function to delete a playlist.

        Parameters
        ----------
        playlist_ : Playlist
            Playlist to delete.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'delete_playlist' method
        return self.database.delete_playlist(playlist_=playlist_)

    # *** REMOVE VIDEO FROM PLAYLIST *** #
    def remove_video_from_playlist(self, video_: Video, playlist_: Playlist) -> dict:

        """
        Remove Video From Playlist
        ==========================
        Function to remove a video from a playlist.

        Parameters
        ----------
        video_ : Video
            Video to remove.

        playlist_ : Playlist
            Playlist to remove the video from.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'remove_video_from_playlist' method
        return self.database.remove_video_from_playlist(video_=video_, playlist_=playlist_)

    # *** ADD VIDEO TO PLAYLIST *** #
    def add_video_to_playlist(self, video_: Video, playlist_: Playlist) -> dict:

        """
        Add Video To Playlist
        =====================
        Function to add a video to a playlist.

        Parameters
        ----------
        video_ : Video
            Video to add.

        playlist_ : Playlist
            Playlist to add the video to.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        # Return the result of 'add_video_to_playlist' method
        return self.database.add_video_to_playlist(video_=video_, playlist_=playlist_)

    # *** UPDATE LIKES *** #
    def update_likes(self, video_: Video, likes: int) -> dict:

        """
        Update Likes
        ============
        Function to update the likes of a video.

        Parameters
        ----------
        video_ : Video
            Video to update.

        likes : int
            Number of likes to update.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        try:
            # Get the index of the video
            index: int = self.database.get_index(video_=video_)
            # Update the likes of the video
            self.database.videos[index].update_likes(likes=likes)
            # Set message
            message = {
                "video": video_,
                "message": "Likes updated successfully",
                "status": 200
            }

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "video": video_.video,
                "message": error,
                "status": 500
            }

        return message

    # *** UPDATE VIEWS *** #
    def update_views(self, video_: Video, views: int) -> dict:

        """
        Update Views
        ============
        Function to update the views of a video.

        Parameters
        ----------
        video_ : Video
            Video to update.

        views : int
            Number of views to update.

        Returns
        -------
        dict
            A dictionary with the result of the operation.
        """

        try:
            # Get the index of the video
            index: int = self.database.get_index(video_=video_)
            # Update the views of the video
            self.database.videos[index].update_views(views=views)
            # Set message
            message = {
                "video": video_,
                "message": "Views updated successfully",
                "status": 200
            }

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "video": video_.video,
                "message": error,
                "status": 500
            }

        return message
