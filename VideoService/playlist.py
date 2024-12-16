from .video import Video

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

    def add_video(self, video: Video) -> None:
        self.videos.append(video.video)

    def remove_video(self, video: Video) -> None:
        self.videos.remove(video.video)
