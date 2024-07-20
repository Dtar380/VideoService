########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS
import json

########################################
#####  CODE                        #####
########################################

#####  CLASSES

# Builds video objects which contain key info of all videos in the database
class Video:

    """
    The class Video is in charge of creating a Video object. A Video object contains all<br>
    data assigned to a video on the DataBase, which was given when uploading to the<br>
    DataBase.
    <br>
    ---
    Every video object requires this properties:
    - **TITLE** (str) - Title assigned to the video on upload
    - **FILENAME** (str) - Name of the file in the videos folder
    - **FILETYPE** (str) - File extension (See <> to see format support)
    - **LENGTH** (int) - Duration of the video in seconds
    ---
    Video objects can also be provided with this properties:
    - **DESCRIPTION** (str) - Description provided on upload
    - **TAGS** (list[str]) - Tags provided on upload
    - **LIKES** (int) - Use if Like system is used
    ---
    The Video Object also contains a property method called video.<br>
    This property method is used to generate and return a dictionary<br>
    which contains all the properties of the object
    """

    # Constructor of the object
    # Sets given parameters to object constants
    def __init__(self,
        TITLE: str,
        FILENAME: str,
        FILETYPE: str,
        LENGTH: int,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        LIKES: int = None
        ) -> None:

        self.TITLE = TITLE
        self.FILENAME = FILENAME
        self.FILETYPE = FILETYPE
        self.LENGTH = LENGTH
        self.DESCRIPTION = DESCRIPTION
        self.TAGS = TAGS
        self.LIKES = LIKES

    # Property that stores a dict with the key values of the video
    @property
    def video(self) -> dict:

        video_json = {
            "TITLE": self.TITLE,
            "FILENAME": self.FILENAME,
            "FILETYPE": self.FILETYPE,
            "LENGTH": self.LENGTH,
            "DESCRIPTION": self.DESCRIPTION,
            "TAGS": self.TAGS,
            "LIKES": self.LIKES
        }

        return video_json

# Builds an object with a list of Video objects inside
class Videos:

    """The class Videos is in charge of storing and managing Video Objects. This is<br>
    done by using a list containing Video Objects. This class access every part of<br>
    the DataBase to create the Video Objects and manage it self.
    ---
    Every video object requires this properties:
    - **DATABASE** (str) - Path to the JSON DataBase file
    - **VIDEOS** (str) - Path to the folder containing the Videos
    ---
    Videos class contains the next methods:
    - **load_videos** - Returns a list made of Video Objects accessing the DataBase
    - **save_videos** - Saves the videos list as a dictionary to the DataBase
    - **add_video** - Appends to the videos list and adds an extra object and saves
    - **delete_video** - Deletes an object from the videos list from a given index
    """

    # Constructor of the object
    # Sets given parameters as constants and creates the videos variable 
    def __init__(self, DATABASE: str, VIDEOS: str) -> None:
        self.DATABASE = DATABASE
        self.VIDEOS = VIDEOS
        self.videos = self.load_videos()

    # Method in charge of loading the database as Video objects in a list
    def load_videos(self) -> list[Video]:
        try:
            with open(self.DATABASE, "r+") as f:
                data = json.loads(f.read())

            return [Video(
                TITLE=video["TITLE"],
                FILENAME=video["FILENAME"],
                FILETYPE=video["FILETYPE"],
                LENGTH=video["LENGTH"],
                DESCRIPTION=video["DESCRIPTION"],
                TAGS=video["TAGS"],
                LIKES=video["LIKES"]
            ) for video in data]
        
        except:
            raise "ERROR [VIDEOS]: Couldn't get the Videos from Videos Class, check DATABASE path."
    
    # Method in charge of saving the Video objects to the JSON database
    def save_videos(self):
        data = [video.video for video in self.videos]

        with open(self.DATABASE, "w+") as f:
            json.dump(data, f, indent=2, separators=(',',':'))

    # Method in charge of adding a video to the videos variable
    def add_video(self,
        TITLE: str,
        FILENAME: str,
        FILETYPE: str,
        LENGTH: int,
        DESCRIPTION: str = None,
        TAGS: list[str] = None,
        LIKES: int = None
        ):

        video = Video(
            TITLE=TITLE,
            FILENAME=FILENAME,
            FILETYPE=FILETYPE,
            LENGTH=LENGTH,
            DESCRIPTION=DESCRIPTION,
            TAGS=TAGS,
            LIKES=LIKES)

        self.videos.append(video)

        self.save_videos()

    # Method for getting index of a video by using FILENAME attribute
    def __get_by_name(self, FILENAME: str) -> int:
        for index, video in enumerate(self.videos):
            if FILENAME == video.video["FILENAME"]:
                return index

        raise "ERROR [VIDEOS]: Given FILENAME was not found or doesn't exist"

    # Method in charge of deleting a Video from the videos list
    def delete_video(self, video_id: int = None, FILENAME: str = None):
        try:
            if video_id:
                del self.videos[video_id]

            elif FILENAME:
                del self.videos[self.__get_by_name(FILENAME=FILENAME)]

            self.save_videos()

        except IndexError:
            raise "ERROR [VIDEOS]: video_id not in range of self.videos"
        
        else:
            raise "ERROR [VIDEOS]: Didn't gave any parameters, a video ID or FILENAME is needed"