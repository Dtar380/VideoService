import json
import os

from .video import Video
from .playlist import Playlist
from .files_manager import FileManager
from .__errors__ import NotFoundError, AlreadyExistsError, error_parser

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

        for i in self.DATABASES:
            if not os.path.exists(f"{self.DATABASE}\\{i}"):
                with open(f"{self.DATABASE}\\{i}", "w") as file:
                    json.dump([], file)

        self.load_videos()
        self.load_playlists()

    # Load videos and playlists from the database
    def load_videos(self) -> list[Video]:
        with open(f"{self.DATABASE}\\videos.json", "r") as file:
            data = json.load(file)
            self.videos = [Video(**video) for video in data]

    def load_playlists(self) -> list[Playlist]:
        with open(f"{self.DATABASE}\\playlists.json", "r") as file:
            data = json.load(file)
            self.playlists = [Playlist(**playlist) for playlist in data]

    # Save videos and playlists to the database
    def save_videos(self) -> None:
        data = [video.__dict__ for video in self.videos]
        with open(f"{self.DATABASE}\\videos.json", "w") as file:
            json.dump(data, file)

    def save_playlists(self) -> None:
        data = [playlist.__dict__ for playlist in self.playlists]
        with open(f"{self.DATABASE}\\playlists.json", "w") as file:
            json.dump(data, file)

    # Add and delete videos and playlists
    def add_video(self, video_: Video) -> None:
        try:
            video_dicts = [video.video for video in self.videos]
            if video_.video not in video_dicts:
                self.videos.append(video_)
            else:
                raise AlreadyExistsError("Video already exists")

        except Exception as error:
            print(error_parser(error))

        self.save_videos()
        return {"video": video_, "message": "Video added successfully"}

    def add_playlist(self, playlist_: Playlist) -> None:
        try:
            playlist_dicts = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist not in playlist_dicts:
                self.playlists.append(playlist_)
            else:
                raise AlreadyExistsError("Video already exists")
            
        except Exception as error:
            print(error_parser(error))

        self.save_playlists()
        return {"playlist": playlist_, "message": "Playlist added successfully"}

    def delete_video(self, video_: Video) -> None:
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
            else:
                raise NotFoundError("Video not found in the database")

        except Exception as error:
            print(error_parser(error))

        self.save_videos()
        return {"video": video_, "message": "Video deleted successfully"}

    def delete_playlist(self, playlist_: Playlist) -> None:
        try:
            playlists = [playlist.playlist for playlist in self.playlists]
            if playlist_.playlist in playlists:
                index = playlists.index(playlist_.playlist)
                self.playlists.pop(index)
            else:
                raise NotFoundError("Playlist not found in the database")

        except Exception as error:
            print(error_parser(error))

        self.save_playlists()
        return {"playlist": playlist_, "message": "Playlist deleted successfully"}
