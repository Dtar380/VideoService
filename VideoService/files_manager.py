
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

# *** External modules *** #
import cv2

# *** Python modules *** #
import shutil
import os
from datetime import datetime

# *** Internal modules *** #
from .video import Video
from .__errors__ import error_parser

#################################################*
##### ***  CODE  ***    #########################*
#################################################*

### *** FILE MANAGER CLASS *** ###
class FileManager:

    """
    FileManager
    ===========
    Manages video and thumbnail files on a server and database.
    """

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        UPLOADS: str = ".\\Uploads",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        """
        Class Constructor
        =================

        Parameters
        ----------
        UPLOADS : str, optional
            The path to the directory where the uploaded files are stored.

        VIDEOS : str, optional
            The path to the directory where the video files are stored.

        THUMBNAILS : str, optional
            The path to the directory where the thumbnail files are stored.
        """

        # Set arguments as class attributes
        self.UPLOADS = UPLOADS
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

    ## *** CLASS METHODS *** ##
    # *** UPLOAD FILE TO SERVER AND DATABASE *** #
    def upload_file(self, **kwargs) -> Video | dict:

        """
        Upload File
        ===========
        Uploads a video and thumbnail files to the server and database.

        Parameters
        ----------
        VIDEO_FILENAME : str
            The name of the video file.

        THUMBNAIL_FILENAME : str, optional
            The name of the thumbnail file.

        TITLE : str
            The title of the video.

        OWNER : str
            The username of the video owner.

        VISIBILITY : str
            The visibility of the video.

        DESCRIPTION : str, optional
            The description of the video.

        TAGS : list, optional
            The tags of the video.

        Returns
        -------
        Video
            The video object if the files are uploaded successfully.

        dict
            A dictionary with an error message if the files are not uploaded.
        """

        # Get the video and thumbnail filenames
        video_filename = kwargs.get("VIDEO_FILENAME") or None
        thumbnail_filename = kwargs.get("THUMBNAIL_FILENAME") or None

        # Check if the video filename is provided
        if not video_filename:
            # Return an error message if the video filename is not provided
            return {
                "message": "ERROR [FileManager]: 'VIDEO_FILENAME' is required",
                "status": 400
            }

        # Get the next index for file naming
        index = self.__get_index()

        # Rename the files
        video_filename = self.__rename_file(
            file = video_filename,
            file_type = "video",
            index = index
        )

        # Check if the thumbnail filename is provided
        if not thumbnail_filename:
            # Create a thumbnail if the thumbnail filename is not provided
            thumbnail_filename = self.__create_thumbnail(
                file = video_filename,
                index = index
            )
        else:
            # Rename the thumbnail file if it is provided
            thumbnail_filename = self.__rename_file(
                file = thumbnail_filename,
                file_type = "thumbnail",
                index = index
            )

        # Upload the files to the database
        self.__upload_to_database([video_filename, thumbnail_filename])

        # Create a video object parameters
        video = {
            "TITLE": kwargs.get("TITLE"),
            "VIDEO_FILENAME": video_filename,
            "VIDEO_FILETYPE": video_filename.split('.')[1],
            "THUMBNAIL_FILENAME": thumbnail_filename,
            "THUMBNAIL_FILETYPE": thumbnail_filename.split('.')[1],
            "UPLOAD_DATE": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "OWNER": kwargs.get("OWNER"),
            "VISIBILITY": kwargs.get("VISIBILITY"),
            "LENGTH": self.__get_length(video_filename),
            "DESCRIPTION": kwargs.get("DESCRIPTION"),
            "TAGS": kwargs.get("TAGS")
        }

        # Return the video object
        return Video(**video)

    # *** DELETE FILE FROM SERVER AND DATABASE *** #
    @staticmethod
    def delete_file(file_name: str, directory: str) -> None:

        """
        Delete File
        ===========
        Deletes a file from the server and database.

        Parameters
        ----------
        file_name : str
            The name of the file to delete.

        directory : str
            The directory where the file is stored.
        """

        try:
            # Get the file path
            file = os.path.join(directory, file_name)
            # Remove the file
            os.remove(file)

        except Exception as error:
            # Print the error message
            print(error_parser(error))

    ## *** PRIVATE METHODS *** ##
    # *** Upload files to the database *** #
    def __upload_to_database(self, files: list) -> None:

        try:
            # Iterate over the files
            for file in files:
                # Set the source and destiny paths
                source_dist = os.path.join(self.UPLOADS, file)
                # Set the destiny path
                destiny_dist = os.path.join(
                    # Check if the file is a video or a thumbnail
                    self.VIDEOS if "video" in file else self.THUMBNAILS,
                    file
                )
                # Move the file to the destiny
                shutil.move(source_dist, destiny_dist)

        except Exception as error:
            # Print the error message
            print(error_parser(error))

    # *** Get the next index for file naming *** #
    def __get_index(self) -> int:
        # Set the index to 0
        index: int = 0

        try:
            # Get the files in the videos directory
            files = os.listdir(self.VIDEOS)
            # Get the last file
            file = files[-1]

            # Get the index from the file name
            index = int(file.split("_")[1].split(".")[0])
            # Check if the index is valid
            if index < 0:
                raise ValueError("ERROR [FileManager]: Invalid index")

        except Exception as error:
            # Print the error message
            print(error_parser(error))

        return index

    # *** Rename the file *** #
    def __rename_file(self, file_name: str, file_type: str, index: int) -> str:
        # Set the new name to None
        new_name: str = ""

        try:
            # Set the paths
            old_dist = os.path.join(self.UPLOADS, file_name) # Set the old path
            new_name = f"{file_type}_{index}.{file_name.split('.')[1]}" # Set the new name
            new_dist = os.path.join(self.UPLOADS, new_name) # Set the new path

            # Rename the file
            os.rename(old_dist, new_dist)

        except Exception as error:
            # Print the error message
            print(error_parser(error))

        return new_name

    # *** Create a thumbnail *** #
    def __create_thumbnail(self, file_name: str, index: int) -> str:
        # Set the new name to None
        new_name: str = ""

        try:
            # Open the video
            video = os.path.join(self.UPLOADS, file_name)
            videoObj = cv2.VideoCapture(video) # Create a video object

            # Check if the video is opened
            if not videoObj.isOpened():
                raise FileNotFoundError("ERROR [FileManager]: Video not found")

            # Get the frame located in the end of the first 10% of the video
            length = videoObj.get(cv2.CAP_PROP_FRAME_COUNT)
            if length == 0:
                raise ValueError("ERROR [FileManager]: Video has no frames")
            frame = length // 10 + 1
            videoObj.set(cv2.CAP_PROP_POS_FRAMES, frame)
            success, image = videoObj.read()

            # Check if the frame was found
            if not success or image is None:
                raise RuntimeError("ERROR [FileManager]: Frame not found")

            # Create the thumbnail
            new_name = f"miniature_{index}.jpg" # Set the new name
            thumbnail_path = os.path.join(self.THUMBNAILS, new_name) # Set the thumbnail path
            cv2.imwrite(thumbnail_path, image) # Save the thumbnail

        except Exception as error:
            # Print the error message
            print(error_parser(error))

        finally:
            # Release the video object
            if 'videoObj' in locals() and videoObj.isOpened():
                videoObj.release()

        return new_name

    # *** Get the video length *** #
    def __get_length(self, file_name: str) -> int:
        # Set the duration to 0
        duration: int = 0

        try:
            # Open the video
            video = os.path.join(self.VIDEOS, file_name)
            videoObj = cv2.VideoCapture(video) # Create a video object

            # Check if the video is opened
            if not videoObj.isOpened():
                raise FileNotFoundError("ERROR [FileManager]: Video not found")

            # Calculate the video duration in seconds using frames and fps
            length = videoObj.get(cv2.CAP_PROP_FRAME_COUNT) # Get the number of frames
            fps = videoObj.get(cv2.CAP_PROP_FPS) # Get the frames per second
            duration = length // fps # Calculate the duration

        except Exception as error:
            # Print the error message
            print(error_parser(error))

        finally:
            # Release the video object
            if 'videoObj' in locals() and videoObj.isOpened():
                videoObj.release()

        return duration
