class FileManager:

    def __init__(self,
        UPLOADS: str = ".\\Uploads",
        VIDEOS: str = ".\\Database\\Videos",
        THUMBNAILS: str = ".\\Database\\THUMBNAILS"
    ) -> None:

        self.UPLOADS = UPLOADS
        self.VIDEOS = VIDEOS
        self.THUMBNAILS = THUMBNAILS

    def upload_file(self, file: str, **kwargs) -> None:
        pass

    def delete_file(self, file: str) -> None:
        pass

    def __move_file(self, file: str, destination: str) -> None:
        pass

    def __rename_file(self, file: str, new_name: str) -> None:
        pass

    def __create_thumbnail(self, file: str) -> None:
        pass

    def __get_length(self, file: str) -> None:
        pass
