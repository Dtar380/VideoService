class Video:

    # Constructor
    def __init__(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        VIDEO_FILETYPE: str,
        THUMBNAIL_FILENAME: str,
        THUMBNAIL_FILETYPE: str,
        UPLOAD_DATE: str,
        OWNER: str,
        VISIBILITY: str,
        LENGTH: int,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        LIKES: int = None,
        VIEWS: int = None
    ) -> None:

        self.TITLE = TITLE
        self.VIDEO_FILENAME = VIDEO_FILENAME
        self.VIDEO_FILETYPE = VIDEO_FILETYPE
        self.THUMBNAIL_FILENAME = THUMBNAIL_FILENAME
        self.THUMBNAIL_FILETYPE = THUMBNAIL_FILETYPE
        self.UPLOAD_DATE = UPLOAD_DATE
        self.LENGTH = LENGTH
        self.OWNER = OWNER
        self.VISIBILITY = VISIBILITY

        self.DESCRIPTION = DESCRIPTION if DESCRIPTION else ""
        self.TAGS = TAGS if TAGS else [""]
        self.LIKES = LIKES or 0
        self.VIEWS = VIEWS if VIEWS else 0

    # Method to be called when printing object
    def __str__(self) -> str:
        return str(self.video)

    # Property that stores a dict with the key values of the video
    @property
    def video(self) -> dict:

        video_json = {
            "TITLE": self.TITLE,
            "VIDEO_FILENAME": self.VIDEO_FILENAME,
            "VIDEO_FILETYPE": self.VIDEO_FILETYPE,
            "THUMBNAIL_FILENAME": self.THUMBNAIL_FILENAME,
            "THUMBNAIL_FILETYPE": self.THUMBNAIL_FILETYPE,
            "UPLOAD_DATE": self.UPLOAD_DATE,
            "LENGTH": self.LENGTH,
            "DESCRIPTION": self.DESCRIPTION,
            "TAGS": self.TAGS,
            "LIKES": self.LIKES
        }

        return video_json

    def update_likes(self, likes: int) -> None:
        self.LIKES += likes

    def update_views(self, views: int) -> None:
        self.VIEWS += views
