
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

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        DATABASE: str,
        VIDEOS: str,
        THUMBNAILS: str,
        UPLOADS: str
    ) -> None:

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

        try:
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
            print(error_parser(error))
            return {"message": "ERROR [VideoService]: Invalid input data"}

        # Return the result of 'add_video' method
        return self.database.add_video(
            # Pass the result of 'upload_file' method as 'video_'
            video_ = self.file_manager.upload_file(
                TITLE=TITLE,
                VIDEO_FILENAME=VIDEO_FILENAME,
                OWNER=OWNER,
                VISIBILITY=VISIBILITY,
                THUMBNAIL_FILENAME=THUMBNAIL_FILENAME,
                DESCRIPTION=DESCRIPTION,
                TAGS=TAGS
            )
        )

    # *** CREATE PLAYLIST *** #
    def create_playlist(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
    ) -> dict:

        try:
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
            print(error_parser(error))
            return {"message": "ERROR [VideoService]: Invalid input data"}

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
        # Return the result of 'save_videos' method
        return self.database.save_videos()

    # *** SAVE PLAYLISTS *** #
    def save_playlists(self) -> dict:
        # Return the result of 'save_playlists' method
        return self.database.save_playlists()

    # *** DELETE VIDEO *** #
    def delete_video(self, video_: Video) -> dict:
        # Return the result of 'delete_video' method
        return self.database.delete_video(video_=video_)

    # *** DELETE PLAYLIST *** #
    def delete_playlist(self, playlist_: Playlist) -> dict:
        # Return the result of 'delete_playlist' method
        return self.database.delete_playlist(playlist_=playlist_)

    # *** REMOVE VIDEO FROM PLAYLIST *** #
    def remove_video_from_playlist(self, video_: Video, playlist_: Playlist) -> dict:
        # Return the result of 'remove_video_from_playlist' method
        return self.database.remove_video_from_playlist(video_=video_, playlist_=playlist_)

    # *** ADD VIDEO TO PLAYLIST *** #
    def add_video_to_playlist(self, video_: Video, playlist_: Playlist) -> dict:
        # Return the result of 'add_video_to_playlist' method
        return self.database.add_video_to_playlist(video_=video_, playlist_=playlist_)

    # *** UPDATE LIKES *** #
    def update_likes(self, video_: Video, likes: int) -> dict:
        try:
            # Get the index of the video
            index: int = self.database.get_index(video_=video_)
            # Update the likes of the video
            self.database.videos[index].update_likes(likes=likes)
            # Set message
            message = {"video": video_, "message": "Likes updated successfully"}

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {"video": video_.video, "message": error}

        return message

    # *** UPDATE VIEWS *** #
    def update_views(self, video_: Video, views: int) -> dict:
        try:
            # Get the index of the video
            index: int = self.database.get_index(video_=video_)
            # Update the views of the video
            self.database.videos[index].update_views(views=views)
            # Set message
            message = {"video": video_, "message": "Views updated successfully"}

        except Exception as error:
            # Parse error and set message
            error = error_parser(error)
            print(error)
            message = {"video": video_.video, "message": error}

        return message
