########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS

# PYTHON BUILT-IN
from typing import List
from os import path, listdir, rename
from shutil import move
from datetime import datetime

# LIBRARIES
import cv2

#####  INTERNAL IMPORTS
from videos import Videos

########################################
#####  CODE                        #####
########################################

# Builds an object in charge of the uploads done to the server
class UploadManager:
    
    """
    UploadManager
    -------------
    The class Upload Manager is in charge of managing the uploads <br>
    that are done to the server.
    
    This class creates an object containing the paths to the Uploads, <br>
    Miniatures and Videos folder and is used to move files between <br>
    folders and indexing uploaded files into the DataBase JSON.
    """

    # Constructor of the object
    # Sets given parameters as class properties
    def __init__(self,
        UPLOADS: str,
        MINIATURES: str,
        VIDEOS: str,
        ) -> None:

        """
        ## Constructor function of UploadManager class

        Parameters
        ----------
        UPLOADS : str
            Path to the Uploads folder

        MINIATURES : str
            Path to the Miniatures folder

        VIDEOS : str
            Path to the Videos folder
        """

        self.UPLOADS = UPLOADS
        self.MINIATURES = MINIATURES
        self.VIDEOS = VIDEOS

    # Method in charge of uploading the files that have been uploaded
    def upload(self,
        videos: Videos,
        TITLE: str,
        VIDEO_FILENAME: str,
        MINIATURE_FILENAME: str = None,
        DESCRIPTION: str = None,
        TAGS: List[str] = None,
        ) -> Videos:

        """
        ## Method used to upload files to the DataBase

        Parameters
        ----------
        videos : Videos
            Information about the Videos DataBase

        TITLE : str
            Title provided for the video

        VIDEO_FILENAME : str
            File name of the video

        MINIATURE_FILENAME : str, optional
            File name of the miniature for the video , by default None

        DESCRIPTION : str, optional
            Description for the video, by default None

        TAGS : list[str], optional
            Tags for the video, by default None
        
        Returns
        -------
        self.videos : Videos
            Contains all info about the DataBase
        """

        index = len(listdir(self.VIDEOS))

        VIDEO_FILENAME=self.__rename_upload(
            file_name=VIDEO_FILENAME,
            file_type="Video",
            index=index
        )

        if not MINIATURE_FILENAME:
            MINIATURE_FILENAME = self.__create_miniature(
                file_name=VIDEO_FILENAME,
                index=index
            )
            
        else:
            MINIATURE_FILENAME = self.__rename_upload(
                file_name=MINIATURE_FILENAME,
                file_type="Miniature",
                index=index
            )

        self.__upload_to_database(file_name=VIDEO_FILENAME)

        videos.add_video(
            TITLE=TITLE,
            VIDEO_FILENAME=VIDEO_FILENAME,
            VIDEO_FILETYPE=VIDEO_FILENAME.split(".")[1],
            MINIATURE_FILENAME=MINIATURE_FILENAME,
            MINIATURE_FILETYPE=MINIATURE_FILENAME.split(".")[1],
            UPLOAD_DATE=datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
            LENGTH=self.__get_length(file_name=VIDEO_FILENAME),
            DESCRIPTION=DESCRIPTION,
            TAGS=TAGS
        )

        return videos

    # Private method for creating a miniature if none was given using first frame of the video
    def __create_miniature(self,
            file_name: str,
            index: int
        ) -> str:
        
        file = path.join(self.VIDEOS, file_name)
        vidObj = cv2.VideoCapture(file)
        success, image = vidObj.read()
        new_name = f"Miniature_{index}.jpg"
        cv2.imwrite(path.join(self.MINIATURES, file_name), image)
        return new_name

    # Private method for renaming uploaded files to have an structured naming order
    def __rename_upload(self,
            file_name: str,
            file_type: str,
            index: int
        ) -> str:

        old_dist = path.join(self.UPLOADS, file_name)
        new_name = f"{file_type}_{index}.{file_name.split(".")[1]}"
        new_dist = path.join(self.UPLOADS, new_name)
        rename(old_dist, new_dist)
        return new_name

    # Private method for getting length of the video in seconds
    def __get_length(self, file_name: str) -> int:
        file = path.join(self.VIDEOS, file_name)
        video = cv2.VideoCapture(file)
        duration = int(video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS))
        return duration

    # Private method used to upload videos from the uploads to the DataBase
    def __upload_to_database(self, file_name: str):
        source_dist = path.join(self.UPLOADS, file_name)
        destiny_dist = path.join(self.VIDEOS, file_name)
        move(source_dist, destiny_dist)