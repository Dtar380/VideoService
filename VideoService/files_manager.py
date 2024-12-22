
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

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

    ## *** CLASS CONSTRUCTOR *** ##
    def __init__(self,
        UPLOADS: str = ".\\Uploads",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        # Set arguments as class attributes
        self.UPLOADS = UPLOADS
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

    ## *** CLASS METHODS *** ##
    # *** UPLOAD FILE TO SERVER AND DATABASE *** #
    def upload_file(self, **kwargs) -> Video | dict:
        # Get the video and thumbnail filenames
        video_filename = kwargs.get("VIDEO_FILENAME") or None
        thumbnail_filename = kwargs.get("THUMBNAIL_FILENAME") or None

        # Check if the video filename is provided
        if not video_filename:
            # Return an error message if the video filename is not provided
            return {"message": "ERROR [FileManager]: 'VIDEO_FILENAME' is required"}

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

    # *** Get the next index for file naming *** #
    def __get_index(self) -> int:
        # Get the files in the videos directory
        files = os.listdir(self.VIDEOS)
        # Get the last file
        file = files[-1]
        # Return the next index according to file naming
        return int(file.split("_")[1].split(".")[0]) + 1

    # *** Rename the file *** #
    def __rename_file(self, file_name: str, file_type: str, index: int) -> str:
        # Set the old destiny
        old_dist = os.path.join(self.UPLOADS, file_name)
        # Set the new name
        new_name = f"{file_type}_{index}.{file_name.split('.')[1]}"
        # Set the new destiny
        new_dist = os.path.join(self.UPLOADS, new_name)
        # Rename the file
        os.rename(old_dist, new_dist)

        return new_name

    # *** Create a thumbnail *** #
    def __create_thumbnail(self, file_name: str, index: int) -> str:
        # Get the video path
        video = os.path.join(self.UPLOADS, file_name)
        # TODO: Add CV2 logic for creating thumbnails

    # *** Get the video length *** #
    def __get_length(self, file_name: str) -> int:
        # Get the video path
        video = os.path.join(self.VIDEOS, file_name)
        # TODO: Add CV2 logic for getting video length
