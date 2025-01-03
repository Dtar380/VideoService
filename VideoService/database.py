
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

# *** Python modules *** #
import json
import os

# *** Internal modules *** #
from .video import Video
from .playlist import Playlist
from .files_manager import FileManager
from .__errors__ import *

#################################################*
##### ***  CODE  ***    #########################*
#################################################*

### *** DATABASE CLASS *** ###
class Database:

    """
    Database
    ========
    The Database class is used to manage the videos and playlists databases.
    """

    ## *** CLASS ATTRIBUTES *** ##
    DATABASES = [
        "videos.json",
        "playlists.json"
    ]

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        DATABASE: str = ".\\Database",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        """
        Class Constructor
        =================

        Parameters
        ----------
        DATABASE : str, optional
            The path to the database directory.

        VIDEOS : str, optional
            The path to the videos directory.

        THUMBNAILS : str, optional
            The path to the thumbnails directory.
        """

        # Set arguments as class attributes
        self.DATABASE = DATABASE
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

        # Check if directories exist
        for database in self.DATABASES:
            if not os.path.exists(f"{self.DATABASE}\\{database}"):
                # Create directories if they don't exist
                with open(f"{self.DATABASE}\\{database}", "w") as file:
                    json.dump([], file)

        # Create directories if they don't exist
        self.load_videos()
        self.load_playlists()

    ## *** CLASS METHODS *** ##
    # *** LOAD VIDEOS *** #
    def load_videos(self) -> None:

        """
        Load Videos
        ===========
        The load_videos method is used to load the videos from the database.
        """

        # Load videos from the database
        with open(f"{self.DATABASE}\\{self.DATABASES[0]}", "r") as file:
            data = json.load(file)
            self.videos = [Video(**video) for video in data]

    # *** LOAD PLAYLISTS *** #
    def load_playlists(self) -> None:

        """
        Load Playlists
        ==============
        The load_playlists method is used to load the playlists from the database.
        """

        # Load playlists from the database
        with open(f"{self.DATABASE}\\{self.DATABASES[1]}", "r") as file:
            data = json.load(file)
            self.playlists = [Playlist(**playlist) for playlist in data]

    # *** SAVE VIDEOS *** #
    def save_videos(self) -> dict:

        """
        Save Videos
        ===========
        The save_videos method is used to save the videos to the database.

        Returns
        -------
        dict
            A dictionary containing a message
        """

        try:
            # Create a list of video dictionaries
            data = [video.video for video in self.videos]
            # Save the videos to the database
            with open(f"{self.DATABASE}\\{self.DATABASES[0]}", "w") as file:
                json.dump(data, file)
            # Set message
            message = {
                "message": "Videos saved successfully",
                "status": 200
            }

        except Exception as error:
            # Print error and return message
            error = error_parser(error)
            print(error)
            message = {
                "message": error,
                "status": 500
            }

        return message

    # *** SAVE PLAYLISTS *** #
    def save_playlists(self) -> dict:

        """
        Save Playlists
        ==============
        The save_playlists method is used to save the playlists to the database.

        Returns
        -------
        dict
            A dictionary containing a message.
        """

        try:
            # Create a list of playlist dictionaries
            data = [playlist.playlist for playlist in self.playlists]
            with open(f"{self.DATABASE}\\{self.DATABASES[1]}", "w") as file:
                json.dump(data, file)
            # Set message
            message = {
                "message": "Playlists saved successfully",
                "status": 200
            }

        except Exception as error:
            # Print error and return message
            error = error_parser(error)
            print(error)
            message = {
                "message": error,
                "status": 500
            }

        return message

    # *** ADD VIDEOS *** #
    def add_video(self, video_: Video) -> dict:

        """
        Add Video
        =========
        The add_video method is used to add a video to the database.

        Parameters
        ----------
        video_ : Video
            The video object to be added to the database.

        Returns
        -------
        dict
            A dictionary containing the video object and a message.
        """

        try:
            # Create a list of video dictionaries
            video_dicts = [video.video for video in self.videos]
            # Check if video already exists
            if video_.video not in video_dicts:
                # Add video to the database
                self.videos.append(video_)
                # Set message
                message = {
                    "video": video_,
                    "message": "Video added successfully",
                    "status": 200
                }
            else:
                raise AlreadyExistsError("ERROR [DataBase]: Video already exists")

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "video": video_.video,
                "message": error,
                "status": 500
            }

        # Save the videos to the database
        self.save_videos()
        return message

    # *** ADD PLAYLISTS *** #
    def add_playlist(self, playlist_: Playlist) -> dict:

        """
        Add Playlist
        ============
        The add_playlist method is used to add a playlist to the database.

        Parameters
        ----------
        playlist_ : Playlist
            The playlist object to be added to the database.

        Returns
        -------
        dict
            A dictionary containing the playlist object and a message.
        """

        try:
            # Create a list of playlist dictionaries
            playlist_dicts = [playlist.playlist for playlist in self.playlists]
            # Check if playlist already exists
            if playlist_.playlist not in playlist_dicts:
                # Add playlist to the database
                self.playlists.append(playlist_)
                message = {
                    "playlist": playlist_,
                    "message": "Playlist added successfully",
                    "status": 200
                }
            else:
                raise AlreadyExistsError("ERROR [DataBase]: Video already exists")

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "playlist": playlist_.playlist,
                "message": error,
                "status": 500
            }

        # Save the playlists to the database
        self.save_playlists()
        return message

    # *** DELETE VIDEOS *** #
    def delete_video(self, video_: Video) -> dict:

        """
        Delete Video
        ============
        The delete_video method is used to delete a video from the database.

        Parameters
        ----------
        video_ : Video
            The video object to be deleted from the database.

        Returns
        -------
        dict
            A dictionary containing the video object and a message.
        """

        try:
            # Create a list with the video and thumbnail filenames
            files = [
                [video_.video.get("VIDEO_FILENAME"), self.VIDEOS],
                [video_.video.get("THUMBNAIL_FILENAME"), self.THUMBNAILS]
            ]

            # Check if files exist
            for file in files:
                if file[0] not in os.listdir(file[1]):
                    raise FileNotFoundError("ERROR [DataBase]: File not found in the directory")
                FileManager.delete_file(*file)

            # Get the video index
            index = self.get_index(video_=video_)
            # Delete the video
            self.videos.pop(index)
            # Set message
            message = {
                "video": video_,
                "message": "Video deleted successfully",
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

        # Save the videos to the database
        self.save_videos()
        return message

    # *** DELETE PLAYLISTS *** #
    def delete_playlist(self, playlist_: Playlist) -> dict:

        """
        Delete Playlist
        ===============
        The delete_playlist method is used to delete a playlist from the database.

        Parameters
        ----------
        playlist_ : Playlist
            The playlist object to be deleted from the database.

        Returns
        -------
        dict
            A dictionary containing the playlist object and a message
        """

        try:
            # Get the playlist index
            index = self.get_index(playlist_=playlist_)
            # Delete the playlist
            self.playlists.pop(index)
            # Set message
            message = {
                "playlist": playlist_,
                "message": "Playlist deleted successfully",
                "status": 200
            }

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "playlist": playlist_.playlist,
                "message": error,
                "status": 500
            }

        # Save the playlists to the database
        self.save_playlists()
        return message

    # *** ADD VIDEO TO PLAYLIST *** #
    def add_video_to_playlist(self, playlist_: Playlist, video_: Video) -> dict:

        """
        Add Video to Playlist
        =====================
        The add_video_to_playlist method is used to add a video to a playlist.

        Parameters
        ----------
        playlist_ : Playlist
            The playlist object to add the video to.

        video_ : Video
            The video object to be added to the playlist.

        Returns
        -------
        dict
            A dictionary containing the playlist object and a message.
        """

        try:
            # Get the playlist index
            index: int = self.get_index(playlist_=playlist_)
            # Add video to playlist
            self.playlists[index].add_video(video_)
            # Set message
            message = {
                "playlist": playlist_,
                "message": "Video added to playlist successfully",
                "status": 200
            }

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "playlist": playlist_.playlist,
                "message": error,
                "status": 500
            }

        # Save the playlists to the database
        self.save_playlists()
        return message

    # *** REMOVE VIDEO FROM PLAYLIST *** #
    def remove_video_from_playlist(self, playlist_: Playlist, video_: Video) -> dict:

        """
        Remove Video from Playlist
        ==========================
        The remove_video_from_playlist method is used to remove a video from a playlist.

        Parameters
        ----------
        playlist_ : Playlist
            The playlist object to remove the video from.

        video_ : Video
            The video object to be removed from the playlist.

        Returns
        -------
        dict
            A dictionary containing the playlist object and a message.
        """

        try:
            # Get the playlist index
            index: int = self.get_index(playlist_=playlist_)
            # Remove video from playlist
            self.playlists[index].remove_video(video_)
            # Set message
            message = {
                "playlist": playlist_,
                "message": "Video removed from playlist successfully",
                "status": 200
            }

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {
                "playlist": playlist_.playlist,
                "message": error,
                "status": 500
            }

        # Save the playlists to the database
        self.save_playlists()
        return message

    # *** GET INDEX *** #
    def get_index(self, video_: Video, playlist_: Video) -> int:

        """
        Get Index
        =========
        The get_index method is used to get the index of a video or playlist.

        Parameters
        ----------
        video_ : Video
            The video object to get the index of.

        playlist_ : Playlist
            The playlist object to get the index of.

        Returns
        -------
        int
            The index of the video or playlist.
        """

        # Check if video or playlist is provided
        if video_:
            # Get the video index
            return self.__get_video_index(video_)
        elif playlist_:
            # Get the playlist index
            return self.__get_playlist_index(playlist_)

    ## *** PRIVATE METHODS *** ##
    # *** GET VIDEO INDEX *** #
    def __get_video_index(self, video_: Video) -> int:
        # Create a list of video filenames
        videos = [video.video for video in self.videos]
        # Check if video exists
        if video_.video in videos:
            return videos.index(video_.video)
        else:
            raise NotFoundError("ERROR [DataBase]: Video not found in the database")

    # *** GET PLAYLIST INDEX *** #
    def __get_playlist_index(self, playlist_: Playlist) -> int:
        # Create a list of playlist filenames
        playlists = [playlist.playlist for playlist in self.playlists]
        # Check if playlist exists
        if playlist_.playlist in playlists:
            return playlists.index(playlist_.playlist)
        else:
            raise NotFoundError("ERROR [DataBase]: Playlist not found in the database")
