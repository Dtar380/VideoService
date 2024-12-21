import json
import os

from .video import Video
from .playlist import Playlist
from .files_manager import FileManager
from .__errors__ import *

class Database:

    DATABASES = [
        "videos.json",
        "playlists.json"
    ]

    # Constructor
    def __init__(self,
        DATABASE: str = ".\\Database",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        self.DATABASE = DATABASE
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

        for database in self.DATABASES:
            if not os.path.exists(f"{self.DATABASE}\\{database}"):
                with open(f"{self.DATABASE}\\{database}", "w") as file:
                    json.dump([], file)

        self.load_videos()
        self.load_playlists()

    # Load videos and playlists from the database
    def load_videos(self) -> None:
        with open(f"{self.DATABASE}\\{self.DATABASES[0]}", "r") as file:
            data = json.load(file)
            self.videos = [Video(**video) for video in data]

    def load_playlists(self) -> None:
        with open(f"{self.DATABASE}\\{self.DATABASES[1]}", "r") as file:
            data = json.load(file)
            self.playlists = [Playlist(**playlist) for playlist in data]

    # Save videos and playlists to the database
    def save_videos(self) -> dict:
        try:
            data = [video.video for video in self.videos]
            with open(f"{self.DATABASE}\\{self.DATABASES[0]}", "w") as file:
                json.dump(data, file)

        except Exception as error:
            print(error_parser(error))
            return {"message": "An error occurred while saving the videos"}

        return {"message": "Videos saved successfully"}

    def save_playlists(self) -> dict:
        try:
            data = [playlist.playlist for playlist in self.playlists]
            with open(f"{self.DATABASE}\\{self.DATABASES[1]}", "w") as file:
                json.dump(data, file)

        except Exception as error:
            print(error_parser(error))
            return {"message": "An error occurred while saving the playlists"}

        return {"message": "Playlists saved successfully"}

    # Add and delete videos and playlists
    def add_video(self, video_: Video) -> dict:
        try:
            video_dicts = [video.video for video in self.videos]
            if video_.video not in video_dicts:
                self.videos.append(video_)
                message = {"video": video_, "message": "Video added successfully"}
            else:
                raise AlreadyExistsError("Video already exists")

        except Exception as error:
            print(error_parser(error))
            message = {"video": video_, "message": "Video already exists"}

        self.save_videos()
        return message

    def add_playlist(self, playlist_: Playlist) -> dict:
        try:
            playlist_dicts = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist not in playlist_dicts:
                self.playlists.append(playlist_)
                message = {"playlist": playlist_, "message": "Playlist added successfully"}
            else:
                raise AlreadyExistsError("Video already exists")

        except Exception as error:
            print(error_parser(error))
            message = {"playlist": playlist_, "message": "Playlist already exists"}

        self.save_playlists()
        return message

    def delete_video(self, video_: Video) -> dict:
        try:
            files = [
                [video_.video.get("VIDEO_FILENAME"), self.VIDEOS],
                [video_.video.get("THUMBNAIL_FILENAME"), self.THUMBNAILS]
            ]

            for file in files:
                if file[0] not in os.listdir(file[1]):
                    raise NotFoundError("File not found in the directory")
                FileManager.delete_file(*file)

            videos = [video.video for video in self.videos]
            if video_.video in videos:
                index = videos.index(video_.video)
                self.videos.pop(index)
                message = {"video": video_, "message": "Video deleted successfully"}
            else:
                raise NotFoundError("Video not found in the database")

        except Exception as error:
            print(error_parser(error))
            message = {"video": video_, "message": "Video not found in the database"}

        self.save_videos()
        return message

    def delete_playlist(self, playlist_: Playlist) -> dict:
        try:
            playlists = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist in playlists:
                index = playlists.index(playlist_.playlist)
                self.playlists.pop(index)
                message = {"playlist": playlist_, "message": "Playlist deleted successfully"}
            else:
                raise NotFoundError("Playlist not found in the database")

        except Exception as error:
            print(error_parser(error))
            message = {"playlist": playlist_, "message": "Playlist not found in the database"}

        self.save_playlists()
        return message

    # Add and remove videos from playlists
    def add_video_to_playlist(self, playlist_: Playlist, video_: Video) -> dict:
        try:
            playlists = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist in playlists:
                index = playlists.index(playlist_.playlist)
                self.playlists[index].add_video(video_)
                message = {"playlist": playlist_, "message": "Video added to playlist successfully"}
            else:
                raise NotFoundError("Playlist not found in the database")

        except Exception as error:
            print(error_parser(error))
            if "NotFoundError" in error_parser(error):
                message = {"playlist": playlist_, "message": "Playlist not found in the database"}
            else:
                message = {"playlist": playlist_, "message": "Video already in playlist"}

        self.save_playlists()
        return message

    def remove_video_from_playlist(self, playlist_: Playlist, video_: Video) -> dict:
        try:
            playlists = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist in playlists:
                index = playlists.index(playlist_.playlist)
                self.playlists[index].remove_video(video_)
                message = {"playlist": playlist_, "message": "Video removed from playlist successfully"}
            else:
                raise NotFoundError("Playlist not found in the database")

        except Exception as error:
            print(error_parser(error))
            if "NotFoundError" in error_parser(error):
                message = {"playlist": playlist_, "message": "Playlist not found in the database"}
            else:
                message = {"playlist": playlist_, "message": "Video not found in playlist"}

        self.save_playlists()
        return message
