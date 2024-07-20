########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS

# Python built-in libraries
from os import path, listdir, rename
from shutil import move
import asyncio

# Installed libraries
import cv2

#####  INTERNAL IMPORTS
from videos import Videos

########################################
#####  CODE                        #####
########################################

# Builds an object in charge of the uploads done to the server
class UploadManager:

    """The class UploadsManager is in charge of managing the uploads that are done to the server.
    This class every folder DataBase related and has the ability to move folders and rename files.
    ---
    Every UploadManager object requires this properties:
    - **videos** (Videos) - Videos type object, contains all info about the videos in the server
    - **UPLOADS** - Path to the folder containing the Uploads
    - **MINIATURES** - Path to the folder containing the Miniatures
    - **VIDEOS** - Path to the folder containing the Videos
    ---
    UploadManager only has one public method:
    - **Upload** - Gets the uploaded files, structures them and moves them to the DataBase folders
    """

    # Constructor of the object
    # Sets given parameters as class properties
    def __init__(self,
        UPLOADS: str,
        MINIATURES: str,
        VIDEOS: str,
        videos: Videos,
        ) -> None:

        self.videos = videos
        self.UPLOADS = UPLOADS
        self.MINIATURES = MINIATURES
        self.VIDEOS = VIDEOS

    # Method in charge of uploading the files that have been uploaded
    def upload(self,
        TITLE: str,
        VIDEO_FILENAME: str,
        MINIATURE_FILENAME: str = None,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        ) -> Videos:

        index = len(listdir(self.VIDEOS))

        VIDEO_FILENAME=self.__rename_upload(file_name=VIDEO_FILENAME, file_type="Video", index=index)

        if not MINIATURE_FILENAME:
            MINIATURE_FILENAME = self.__create_miniature(file_name=VIDEO_FILENAME, index=index)
        else:
            MINIATURE_FILENAME = self.__rename_upload(file_name=MINIATURE_FILENAME, file_type="Miniature", index=index)

        self.__upload_to_database(file_name=VIDEO_FILENAME)

        self.videos.add_video(
            TITLE=TITLE,
            VIDEO_FILENAME=VIDEO_FILENAME,
            VIDEO_FILETYPE=VIDEO_FILENAME.split(".")[1],
            MINIATURE_FILENAME=MINIATURE_FILENAME,
            MINIATURE_FILETYPE=MINIATURE_FILENAME.split(".")[1],
            LENGTH=self.__get_length(file_name=VIDEO_FILENAME),
            DESCRIPTION=DESCRIPTION,
            TAGS=TAGS
        )

        return self.videos

    # Private method for creating a miniature if none was given using first frame of the video
    def __create_miniature(self, file_name: str, index: int) -> str:
        file = path.join(self.VIDEOS, file_name)
        vidObj = cv2.VideoCapture(file)
        success, image = vidObj.read()
        new_name = f"Miniature_{index}.jpg"
        cv2.imwrite(path.join(self.MINIATURES, file_name), image)
        return new_name

    # Private method for renaming uploaded files to have an structured naming order
    def __rename_upload(self, file_name: str, file_type: str, index: int) -> str:
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