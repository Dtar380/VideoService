
#################################################*
##### ***  CODE  ***    #########################*
#################################################*

### *** VIDEO CLASS *** ###
class Video:

    """
    Video
    =====
    A class to represent a video.
    """

    ## *** CLASS CONSTRUCTOR *** ##
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

        """
        Class Constructor
        =================

        Parameters
        ----------
        TITLE : str
            The title of the video.

        VIDEO_FILENAME : str
            The filename of the video.

        VIDEO_FILETYPE : str
            The filetype of the video.

        THUMBNAIL_FILENAME : str
            The filename of the thumbnail.

        THUMBNAIL_FILETYPE : str
            The filetype of the thumbnail.

        UPLOAD_DATE : str
            The upload date of the video.

        OWNER : str
            The owner of the video.

        VISIBILITY : str
            The visibility of the video.

        LENGTH : int
            The length of the video.

        DESCRIPTION : str, optional
            The description of the video.

        TAGS : list[str], optional
            The tags of the video.

        LIKES : int, optional
            The likes of the video.

        VIEWS : int, optional
            The views of the video.
        """

        # Set arguments as class attributes
        self.TITLE = TITLE
        self.VIDEO_FILENAME = VIDEO_FILENAME
        self.VIDEO_FILETYPE = VIDEO_FILETYPE
        self.THUMBNAIL_FILENAME = THUMBNAIL_FILENAME
        self.THUMBNAIL_FILETYPE = THUMBNAIL_FILETYPE
        self.UPLOAD_DATE = UPLOAD_DATE
        self.LENGTH = LENGTH
        self.OWNER = OWNER
        self.VISIBILITY = VISIBILITY
        # Set optional arguments as class attributes
        self.DESCRIPTION = DESCRIPTION or ""
        self.TAGS = TAGS or [""]
        self.LIKES = LIKES or 0
        self.VIEWS = VIEWS or 0

    ## *** CLASS PROPERTIES *** ##
    # *** VIDEO JSON *** #
    @property
    def video(self) -> dict:

        """
        Video JSON
        ==========
        Get a JSON object representing the video.

        Returns
        -------
        dict
            A JSON object representing the video.
        """

        # Create a video JSON object
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

    ## *** CLASS METHODS *** ##
    # *** STRING REPRESENTATION *** #
    def __str__(self) -> str:
        return str(self.video)

    # *** UPDATE LIKES *** #
    def update_likes(self, likes: int) -> None:

        """
        Update Likes
        ============
        Update the likes of the video.

        Parameters
        ----------
        likes : int
            The number of likes to add to the video.
        """

        self.LIKES += likes

    # *** UPDATE VIEWS *** #
    def update_views(self, views: int) -> None:

        """
        Update Views
        ============
        Update the views of the video.

        Parameters
        ----------
        views : int
            The number of views to add to the video.
        """

        self.VIEWS += views
