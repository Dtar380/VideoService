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
The class UploadsManager is in charge of managing the uploads that are done 
to the server. This class every folder DataBase related and has the ability 
to move folders and rename files.

Every UploadManager object requires this properties:
- videos (Videos) - Videos type object, contains all info about the videos in the server
- UPLOADS - Path to the folder containing the Uploads
- MINIATURES - Path to the folder containing the Miniatures
- VIDEOS - Path to the folder containing the Videos

UploadManager only has one public method:
- Upload - Gets the uploaded files, structures them and moves them to the DataBase folders
    
```

### **videos**

- #### **Class Video**
```
The class Video is in charge of creating a Video object. A Video object
contains all data assigned to a video on the DataBase, which was given
when uploading to the DataBase.

This object requires the next properties:
- TITLE (str) - Title assigned to the video on upload
- VIDEO_FILENAME (str) - Name of the file of the video
- VIDEO_FILETYPE (str) - File extension of the video
- MINIATURE_FILENAME (str) - Name of the file of the miniature
- MINIATURE_FILETYPE (str) - File extension of the miniature
- LENGTH (int) - Duration of the video in seconds

Video objects can also be provided with this properties:
- DESCRIPTION (str) - Description provided on upload
- TAGS (list[str]) - Tags provided on upload
- LIKES (int) - Use if Like system is used

The Video Object also contains a property method called video.
This property method is used to generate and return a dictionary
which contains all the properties of the object
```

- #### **Class Videos**
```
The class Videos is in charge of storing and managing Video Objects. This is 
done by using a list containing Video Objects. This class access every part 
of the DataBase to create the Video Objects and manage it self.

Every video object requires this properties:
- DATABASE (str) - Path to the JSON DataBase file
- MINIATURES (str) - Path to the folder containing the Miniatures
- VIDEOS (str) - Path to the folder containing the Videos

Videos class contains the next methods:
- load_videos - Returns a list made of Video Objects accessing the DataBase
- save_videos - Saves the videos list as a dictionary to the DataBase
- add_video - Appends to the videos list and adds an extra object and saves
- delete_video - Deletes an object from the videos list from a given index
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
