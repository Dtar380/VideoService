from .video import Video
from .__errors__ import *

class Playlist:

    def __init__(self,
        TITLE: str,
        OWNER: str,
        VISIBILITY: str,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        VIDEOS: list[dict] = None
    ) -> None:

        self.TITLE = TITLE
        self.OWNER = OWNER
        self.VISIBILITY = VISIBILITY

        self.DESCRIPTION = DESCRIPTION if DESCRIPTION else ""
        self.TAGS = TAGS if TAGS else [""]

        if VIDEOS:
            self.videos = VIDEOS
        else:
            self.videos = []

    def __str__(self) -> str:
        return str(self.playlist)

    @property
    def playlist(self) -> dict:

        playlist_json = {
            "TITLE": self.TITLE,
            "OWNER": self.OWNER,
            "VISIBILITY": self.VISIBILITY,
            "DESCRIPTION": self.DESCRIPTION,
            "TAGS": self.TAGS,
            "VIDEOS": self.videos
        }

        return playlist_json

    def add_video(self, video_: Video) -> None:
        try:
            videos = [video for video in self.videos]
            if video_.video in videos:
                raise AlreadyExistsError("ERROR [Playlist]: The video already exists in the playlist")
            else:
                self.videos.append(video_.video)

        except Exception as error:
            error_parser(error)

    def remove_video(self, video: Video) -> None:
        try:
            videos = [video for video in self.videos]
            if video.video in videos:
                self.videos.remove(video.video)
            else:
                raise NotFoundError("ERROR [Playlist]: The video does not exist in the playlist")

        except Exception as error:
            error_parser(error)
