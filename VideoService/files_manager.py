from shutil import move
from os import path, listdir, rename, remove
from datetime import datetime

from .video import Video

class FileManager:

    def __init__(self,
        UPLOADS: str = ".\\Uploads",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        self.UPLOADS = UPLOADS
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

    def upload_file(self, **kwargs) -> Video | None:
        video_filename = kwargs.get("VIDEO_FILENAME") or None
        thumbnail_filename = kwargs.get("THUMBNAIL_FILENAME") or None

        if not video_filename:
            return None

        index = len(listdir(self.VIDEOS))

        video_filename = self.__rename_file(
            file = video_filename,
            file_type = "video",
            index = index
        )

        if not thumbnail_filename:
            thumbnail_filename = self.__create_thumbnail(
                file = video_filename,
                index = index
            )
        else:
            thumbnail_filename = self.__rename_file(
                file = thumbnail_filename,
                file_type = "thumbnail",
                index = index
            )

        self.__upload_to_database([video_filename, thumbnail_filename])

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

        return Video(**video)

    @staticmethod
    def delete_file(file_name: str, directory: str) -> None:
        try:
            file = path.join(directory, file_name)
            remove(file)
        except:
            pass # ! Give an error here

    def __upload_to_database(self, files: list) -> None:
        for file in files:
            source_dist = path.join(self.UPLOADS, file)
            destiny_dist = path.join(
                self.VIDEOS if "video" in file else self.THUMBNAILS,
                file
            )
            move(source_dist, destiny_dist)

    def __rename_file(self, file_name: str, file_type: str, index: int) -> str:
        old_dist = path.join(self.UPLOADS, file_name)
        new_name = f"{file_type}_{index}.{file_name.split('.')[1]}"
        new_dist = path.join(self.UPLOADS, new_name)
        rename(old_dist, new_dist)
        return new_name

    def __create_thumbnail(self, file_name: str, index: int) -> str:
        file = path.join(self.UPLOADS, file_name)
        # ! Add CV2 logic for creating thumbnails

    def __get_length(self, file_name: str) -> int:
        file = path.join(self.VIDEOS, file_name)
        # ! Add CV2 logic for getting video length
