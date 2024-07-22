<p align="center">
    <img src="assets/logo.png">
</p>
<br>

---

# :vhs: **VideoService**

## **The library you needed to create your own Video Service**
**VideoService** is a python library focused on the BackEnd for Video Services, such as YouTube (Note that this library is not used in YouTube, it is just an example). <br>
**VideoService** uses a JSON DataBase to manage all the Videos on the server and its not dependant on external libraries to work, all functionalities depend on bare Python libraries.

## :bookmark_tabs: **Table of Content**
- [**Main features**](#blue_heart-main-features)
- [**Install package**](#arrow_down-install-package)
- [**Working On**](#memo-working-on)
- [**Documentation**](#clipboard-documentation)
- [**Known Issues**](#open_file_folder-known-issues)
- [**License**](#scroll-license)
- [**Sponsorship**](#money_with_wings-sponsorship)

---

## :blue_heart: Main Features
- **Managing Video Files**
- **Managing Data Bases**
- **Search Engine**
    - KeyWord search
    - MultiFilter search
        - Length
        - Tags
        - Order
    - Reputation system

## :arrow_down: Install package

#### Make sure you running on Python 3.12 (No support for other versions now)

### PIP
- #### **If you want user intended version, run:**`pip install VideoService`
- #### **If you want tester intended version, run:** `pip install VideoService[dev]`

### Cloning repository
1. **Clone this repository or download it**
2. **Put the VideoService folder on your project folder**
3. **You're good to go**

## :memo: Working On
Im currently working on the search engine [file is **search_engine.py**]<br>
As there hasn't been a deploy yet, Im not trying to find bugs, Im just coding and testing

When I finish the 3.12 version I'll first give support for older python versions (Probably up to 3.8)<br>
Im also thinking about adding a PlayLists/Series support, but that will be seen when I deploy the library.

## :clipboard: Documentation
Here is an extensive documentation of how VideoService library works and how to use it.

### :bookmark_tabs: **INDEX**
- [**VideoService**](#videoservice)
    - ON WORK
- [**uploads_manager**](#uploads_manager)
- [**videos**](#videos)
    - [class Video](#class-video)
    - [class Videos](#class-videos)
- [**search_engine**](#search_engine)
    - ON WORK

### **VideoService**
```
ON WORK
```

### **uploads_manager**
```
UploadManager : class
----------
The class Upload Manager is in charge of managing the uploads
that are done to the server.

This class creates an object containing the paths to the Uploads,
Miniatures and Videos folder and is used to move files between
folders and indexing uploaded files into the DataBase JSON.

Parameters
----------
    UPLOADS : str
    Path to the Uploads folder

    MINIATURES : str
    Path to the Miniatures folder

    VIDEOS : str
    Path to the Videos folder

    videos : Videos
    Contains all info about the DataBase
----------

Upload : method
----------
Method used to upload files to the DataBase

Parameters
----------
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
```

### **videos**

- #### **Class Video**
```
Video : class
----------
The Video object contains all data assigned to a video on the
DataBase given when uploaded to the server.

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
----------

Video : property
----------
Video object to dict

This property takes all values assigned to the object and<br>
transforms them into a dict

Returns
-------
    video_json : dict
    Contains all info about the Video object
```

- #### **Class Videos**
```
Videos
----------
The Videos object contains all the videos contained in the DataBase 
by using Video objects.

Parameters
----------
    DATABASE : str
    Path to the DataBase JSON file

    MINIATURES : str
    Path to the Miniatures folder

    VIDEOS : str
    Path to the Videos folder
----------

Load Videos
----------
Method used to load videos from the DataBase

Load_videos access the DataBase JSON file and loads all the data in
it to Video objects and dumps them into a list.

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
----------

Save Videos
----------
Method used to save videos to the DataBase

Save_videos transforms the videos list to a dictionary to then save
it to the DataBase JSON file.

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
----------

Add Videos
----------
Method used to add videos to the DataBase

Add_video creates a new Video object and appends it to the videos
list. It then uses save_video function to save the new video added
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
----------

Delete Video
----------
Method used to delete videos from the DataBase

Delete_video deletes a video from the videos list given specific parameters.

Parameters
----------
    VIDEO_ID : int, optional
    Index that leads to the video on the videos list, by default None

    VIDEO_FILENAME : str, optional
    Filename of the video, by default None

Requires only one of both parameter
```

### **search_engine**
```
ON WORK
```

## :open_file_folder: Known Issues
As there hasn't been a deploy yet, Im not trying to find bugs, Im just coding and testing

## :scroll: License
VideoService is distributed under the license MIT.<br>
See the [LICENSE](LICENSE) file for more information.

## :money_with_wings: Sponsorship
You can support me and the project with a donation to my Ko-Fi<br>

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H4TBMEZ)
