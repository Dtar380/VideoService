import os

from .database import Database
from .files_manager import FileManager

from .video import Video
from .playlist import Playlist

from .__errors__ import *

class VideoService:

    def __init__(self,
        DATABASE: str,
        VIDEOS: str,
        THUMBNAILS: str,
        UPLOADS: str
    ) -> None:

        for value in [DATABASE, VIDEOS, THUMBNAILS, UPLOADS]:
            if not isinstance(value, str):
                raise TypeError("ERROR [VideoService]: All values must be of type 'str'")
            if not os.path.exists(value):
                raise NotFoundError(f"ERROR [VideoService]: The path '{value}' does not exist")

        self.DB_PATH = DATABASE
        self.VIDEOS_PATH = VIDEOS
        self.THUMBNAILS_PATH = THUMBNAILS
        self.UPLOADS_PATH = UPLOADS

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

    def upload(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        OWNER: str,
        VISIBILITY: str,
        THUMBNAIL_FILENAME: str = None,
        DESCRIPTION: str = None,
        TAGS: list[str] = None
    ) -> None:

        try:
            for value in [TITLE, VIDEO_FILENAME, OWNER, VISIBILITY, THUMBNAIL_FILENAME, DESCRIPTION]:
                if value and not isinstance(value, str):
                    raise TypeError("ERROR [VideoService]: All values must be of type 'str'")
            if TAGS:
                if not isinstance(TAGS, list):
                    raise TypeError("ERROR [VideoService]: 'TAGS' must be of type 'list'")
                if not all(isinstance(tag, str) for tag in TAGS):
                    raise TypeError("ERROR [VideoService]: All values in 'TAGS' must be of type 'str'")

            if not os.path.isfile(os.path.join(self.UPLOADS_PATH, VIDEO_FILENAME)):
                raise NotFoundError(f"ERROR [VideoService]: The file '{VIDEO_FILENAME}' does not exist")
            if THUMBNAIL_FILENAME and not os.path.isfile(os.path.join(self.UPLOADS_PATH, THUMBNAIL_FILENAME)):
                raise NotFoundError(f"ERROR [VideoService]: The file '{THUMBNAIL_FILENAME}' does not exist")

        except Exception as error:
            print(error_parser(error))
            return {"message": "ERROR [VideoService]: Invalid input data"}

        return self.database.add_video(
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

    def create_playlist(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
    ) -> dict:

        try:
            for value in [TITLE, OWNER, VISIBILITY, DESCRIPTION]:
                if value and not isinstance(value, str):
                    raise TypeError("ERROR [VideoService]: All values must be of type 'str'")
            if TAGS:
                if not isinstance(TAGS, list):
                    raise TypeError("ERROR [VideoService]: 'TAGS' must be of type 'list'")
                if not all(isinstance(tag, str) for tag in TAGS):
                    raise TypeError("ERROR [VideoService]: All values in 'TAGS' must be of type 'str'")

        except Exception as error:
            print(error_parser(error))
            return {"message": "ERROR [VideoService]: Invalid input data"}

        return self.database.add_playlist(
            playlist_ = Playlist(
                TITLE=TITLE,
                OWNER=OWNER,
                VISIBILITY=VISIBILITY,
                DESCRIPTION=DESCRIPTION,
                TAGS=TAGS
            )
        )

    def save_videos(self) -> dict:
        return self.database.save_videos()

    def save_playlists(self) -> dict:
        return self.database.save_playlists()

    def delete_video(self, video_: Video) -> dict:
        return self.database.delete_video(video_=video_)

    def delete_playlist(self, playlist_: Playlist) -> dict:
        return self.database.delete_playlist(playlist_=playlist_)

    def remove_video_from_playlist(self, video_: Video, playlist_: Playlist) -> dict:
        return self.database.remove_video_from_playlist(video_=video_, playlist_=playlist_)

    def add_video_to_playlist(self, video_: Video, playlist_: Playlist) -> dict:
        return self.database.add_video_to_playlist(video_=video_, playlist_=playlist_)

    def update_likes(self, video_: Video, likes: int) -> dict:
        try:
            videos = [video.video for video in self.database.videos]
            if video_.video in videos:
                index = videos.index(video_.video)
                self.database.videos[index].update_likes(likes=likes)
                message = {"video": video_, "message": "Likes updated successfully"}
            else:
                raise NotFoundError("Video not found in the database")
        except Exception as error:
            print(error_parser(error))
            message = {"video": video_, "message": "Video not found in the database"}

        return message

    def update_views(self, video_: Video, views: int) -> dict:
        try:
            videos = [video.video for video in self.database.videos]
            if video_.video in videos:
                index = videos.index(video_.video)
                self.database.videos[index].update_views(views=views)
                message = {"video": video_, "message": "Views updated successfully"}
            else:
                raise NotFoundError("Video not found in the database")
        except Exception as error:
            print(error_parser(error))
            message = {"video": video_, "message": "Video not found in the database"}

        return message
