########################################
#####  DOCUMENTATION               #####
########################################

"""
Videos
------
This file contains the class Video and Videos, which are<br>
in charge of managing the Videos DataBase.
"""

########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS

# PYTHON BUILT-IN
from typing import List
import json

########################################
#####  CODE                        #####
########################################

#####  CLASSES

# Builds video objects which contain key info of all videos in the database
class Video:

    """
    Video
    -----
    The Video object contains all data assigned to a video on the<br>
    DataBase given when uploaded to the server.
    """

    # Constructor of the object
    # Sets given parameters to object constants
    def __init__(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        VIDEO_FILETYPE: str,
        MINIATURE_FILENAME: str,
        MINIATURE_FILETYPE: str,
        UPLOAD_DATE: str,
        LENGTH: int,
        DESCRIPTION: str = "",
        TAGS: List[str] = [""],
        LIKES: int = 0
        ) -> None:

        """
        ## Constructor function of Video class

        Parameters
        ----------
        TITLE : str
            Title assigned to the video on upload

        VIDEO_FILENAME : str
            Name of the file of the video

        VIDEO_FILETYPE : str
            File extension of the video

        MINIATURE_FILENAME : str
            Name of the file of the miniature

        MINIATURE_FILETYPE : str
            File extension of the miniature

        UPLOAD_DATE : str
            Date when the video was uploaded

        LENGTH : int
            Duration of the video in seconds

        DESCRIPTION : str, optional
            Description provided on upload, by default None

        TAGS : list[str], optional
            Tags provided on upload, by default None

        LIKES : int, optional
            Use if Like system is used, by default None
        """

        self.TITLE = TITLE
        self.VIDEO_FILENAME = VIDEO_FILENAME
        self.VIDEO_FILETYPE = VIDEO_FILETYPE
        self.MINIATURE_FILENAME = MINIATURE_FILENAME
        self.MINIATURE_FILETYPE = MINIATURE_FILETYPE
        self.UPLOAD_DATE = UPLOAD_DATE
        self.LENGTH = LENGTH
        self.DESCRIPTION = DESCRIPTION
        self.TAGS = TAGS
        self.LIKES = LIKES

    # Method to be called when printing object
    def __str__(self) -> str:

        minutes = int(self.LENGTH / 60)
        seconds = self.LENGTH - (minutes * 60)

        return f"""Video Object:
    TITLE: {self.TITLE}
    VIDEO_FILENAME: {self.VIDEO_FILENAME}
    VIDEO_FILETYPE: {self.VIDEO_FILETYPE}
    MINIATURE_FILENAME: {self.MINIATURE_FILENAME}
    MINIATURE_FILETYPE: {self.MINIATURE_FILETYPE}
    UPLOAD_DATE: {self.UPLOAD_DATE}
    LENGTH: {minutes}m {seconds}s
    DESCRIPTION: {self.DESCRIPTION}
    TAGS: {self.TAGS}
    LIKES: {self.LIKES}"""

    # Property that stores a dict with the key values of the video
    @property
    def video(self) -> dict:

        """
        ## Video object to dict

        This property takes all values assigned to the object and<br>
        transforms them into a dict
        
        Returns
        -------
        video_json : dict
            Contains all info about the Video object
        """

        video_json = {
            "TITLE": self.TITLE,
            "VIDEO_FILENAME": self.VIDEO_FILENAME,
            "VIDEO_FILETYPE": self.VIDEO_FILETYPE,
            "MINIATURE_FILENAME": self.MINIATURE_FILENAME,
            "MINIATURE_FILETYPE": self.MINIATURE_FILETYPE,
            "UPLOAD_DATE": self.UPLOAD_DATE,
            "LENGTH": self.LENGTH,
            "DESCRIPTION": self.DESCRIPTION,
            "TAGS": self.TAGS,
            "LIKES": self.LIKES
        }

        return video_json

# Builds an object with a list of Video objects inside
class Videos:

    """
    Videos
    ------
    The Videos object contains all the videos contained in the DataBase<br>
    by using Video objects.
    """

    # Constructor of the object
    # Sets given parameters as constants and creates the videos variable 
    def __init__(self,
        DATABASE: str,
        MINIATURES: str,
        VIDEOS: str
        ) -> None:

        """
        ## Constructor function of Videos class

        Parameters
        ----------
        DATABASE : str
            Path to the DataBase JSON file

        MINIATURES : str
            Path to the Miniatures folder

        VIDEOS : str
            Path to the Videos folder
        """

        self.DATABASE = DATABASE
        self.MINIATURES = MINIATURES
        self.VIDEOS = VIDEOS

        with open(DATABASE, "r+") as f:
            DataBase_length = len(f.read())

        if len(DataBase_length) <= 6:
            self.videos = self.load_videos()
        else:
            self.videos: List[Video] = []

    # Method in charge of loading the database as Video objects in a list
    def load_videos(self) -> List[Video]:

        """
        ## Method used to load videos from the DataBase

        Load_videos access the DataBase JSON file and loads all the data in it to<br>
        Video objects and dumps them into a list.
        
        Returns
        -------
        videos : list[Video]
            Contains all info about the DataBase
        """

        try:
            with open(self.DATABASE, "r+") as f:
                data = json.loads(f.read())

            return [Video(
                TITLE=video["TITLE"],
                VIDEO_FILENAME=video["VIDEO_FILENAME"],
                VIDEO_FILETYPE=video["VIDEO_FILETYPE"],
                MINIATURE_FILENAME=video["MINIATURE_FILENAME"],
                MINIATURE_FILETYPE=video["MINIATURE_FILETYPE"],
                UPLOAD_DATE=video["UPLOAD_DATE"],
                LENGTH=video["LENGTH"],
                DESCRIPTION=video["DESCRIPTION"],
                TAGS=video["TAGS"],
                LIKES=video["LIKES"]
            ) for video in data]
        
        except:
            raise "ERROR [VIDEOS]: Couldn't get the Videos from Videos Class, check DATABASE path."
    
    # Method in charge of saving the Video objects to the JSON database
    def save_videos(self) -> None:

        """
        ## Method used to save videos to the DataBase

        Save_videos transforms the `videos` list to a dictionary to then save it<br>
        to the DataBase JSON file.
        Automatically performed by the server when a new Video is uploaded.
        """

        data = [video.video for video in self.videos]

        with open(self.DATABASE, "w+") as f:
            json.dump(data, f, indent=2, separators=(',',':'))

    # Method in charge of adding a video to the videos variable
    def add_video(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        VIDEO_FILETYPE: str,
        MINIATURE_FILENAME: str,
        MINIATURE_FILETYPE: str,
        UPLOAD_DATE: str,
        LENGTH: int,
        DESCRIPTION: str = None,
        TAGS: List[str] = None,
        LIKES: int = None
        ) -> None:

        """
        ## Method used to add videos to the DataBase

        Add_video creates a new Video object and appends it to the `videos`<br>
        list. It then uses `save_video` function to save the new video added<br>
        to the DataBase.

        Parameters
        ----------
        TITLE : str
            Title assigned to the video on upload

        VIDEO_FILENAME : str
            Name of the file of the video

        VIDEO_FILETYPE : str
            File extension of the video

        MINIATURE_FILENAME : str
            Name of the file of the miniature

        MINIATURE_FILETYPE : str
            File extension of the miniature

        UPLOAD_DATE : str
            Date when the video was uploaded

        LENGTH : int
            Duration of the video in seconds

        DESCRIPTION : str, optional
            Description provided on upload, by default None

        TAGS : list[str], optional
            Tags provided on upload, by default None

        LIKES : int, optional
            Use if Like system is used, by default None
        """

        video = Video(
            TITLE=TITLE,
            VIDEO_FILENAME=VIDEO_FILENAME,
            VIDEO_FILETYPE=VIDEO_FILETYPE,
            MINIATURE_FILENAME=MINIATURE_FILENAME,
            MINIATURE_FILETYPE=MINIATURE_FILETYPE,
            UPLOAD_DATE=UPLOAD_DATE,
            LENGTH=LENGTH,
            DESCRIPTION=DESCRIPTION,
            TAGS=TAGS,
            LIKES=LIKES
        )

        self.videos.append(video)

        self.save_videos()

    # Private method for getting index of a video by using FILENAME attribute
    def __get_by_name(self, VIDEO_FILENAME: str) -> int:

        for index, video in enumerate(self.videos):
            if VIDEO_FILENAME == video.video["VIDEO_FILENAME"]:
                return index

        raise "ERROR [VIDEOS]: Given FILENAME was not found or doesn't exist"

    # Method in charge of deleting a Video from the videos list
    def delete_video(self,
        VIDEO_ID: int = None,
        VIDEO_FILENAME: str = None
        ) -> None:

        """
        ## Method used to delete videos from the DataBase

        Delete_video deletes a video from the `videos` list given specific parameters.

        Parameters
        ----------
        VIDEO_ID : int, optional
            Index that leads to the video on the `videos` list, by default None

        VIDEO_FILENAME : str, optional
            Filename of the video, by default None

        **Requires only one of both parameter**
        """

        try:
            if VIDEO_ID:
                del self.videos[VIDEO_ID]

            elif VIDEO_FILENAME:
                del self.videos[self.__get_by_name(VIDEO_FILENAME=VIDEO_FILENAME)]

            self.save_videos() 

        except IndexError:
            raise "ERROR [VIDEOS]: video_id not in range of self.videos"
        
        else:
            raise "ERROR [VIDEOS]: Didn't gave any parameters, a video ID or FILENAME is needed"