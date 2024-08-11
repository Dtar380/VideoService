<p align="center">
    <img src="https://raw.githubusercontent.com/Dtar380/VideoService/main/assets/logo.png">
</p>
<br>

---

# :vhs: **VideoService**

## **The library you needed to create your own Video Service**
**VideoService** is a python library focused on the BackEnd for Video Services, such as YouTube (Note that this library is not used in YouTube, it is just an example). <br>
**VideoService** uses a JSON DataBase to manage all the Videos on the server and its not dependant on external libraries to work (except for OpenCV and Lingua), all functionalities depend on bare Python libraries.

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
    - Title Search
    - MultiFilter search
        - Length
        - Tags
        - Order
    - "Reputation system"

## :arrow_down: Install package

#### Make sure you running on Python 3.8 or above

### PIP
- #### **If you want user intended version, run:**`pip install VideoService`
- #### **If you want tester intended version, run:** `pip install VideoService[dev]`

### Cloning repository
1. **Clone this repository or download it**
2. **Put the VideoService folder on your project folder**
3. **You're good to go**

## :memo: Working On
I will add support for PlayLists/Series, on the next version of the library, but first we need the first deploy.<br>
A Languages API will also be released to make it easier to have language support, instead of having the dictionaries in your own server

## :clipboard: Documentation
Here is an extensive documentation of how VideoService library works and how to use it.

### :bookmark_tabs: **INDEX**
- [**VideoService**](#videoservice)
- [**uploads_manager**](#uploads_manager)
- [**videos**](#videos)
    - [class Video](#class-video)
    - [class Videos](#class-videos)
- [**SearchEngine**](#SearchEngine)
    - [search_engine.py](#search_enginepy)
        - [class QueryWords](#class-querywords)
        - [Functions](#functions)
    - [class Search](#class-search)
    - [query settings](#query-settings)

### **VideoService**

```
VIDEO SERVICE
-------------
The library you didn't know you needed 🗿

----

This library gives you all you need to create a video service, Video management,
DataBase management, and an integrated Search Engine.
```

<details>

```
VideoService : class
--------------------
Main class of Video Service library (and the only class you'll need 😉)
This class will manage all the backend of the service, and you will just
need to call it's methods when required by the server.

Parameters
----------
    DATABASE : str
    Path to the DataBase JSON file

    MINIATURES : str
    Path to the Miniatures folder

    VIDEOS : str
    Path to the Videos folder

    UPLOADS : str
    Path to the Uploads folder

    LANGUAGES : str
    Path to the languages DataBase folder

Raise
-----
    ValueError 
    If variable was not the expected type

    DataBaseNotFound
    If DataBase JSON was not found

    FolderNotFound
    If folder was not found
-----

Upload : method
---------------
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

Raise
-----
    ValueError
    If variable was not the expected type

    FolderNotFound
    If folder was not found
-----

Save Videos : method
--------------------
Save_videos transforms the `videos` list to a dictionary to then save it
to the DataBase JSON file.
Automatically performed by the server when a new Video is uploaded.
--------------------

Delete Video : method
---------------------
Method used to delete videos from the DataBase


Parameters
----------
    VIDEO_ID : int, optional
    Index that leads to the video on the `videos` list, by default None

    VIDEO_FILENAME : str, optional
    Filename of the video, by default None

**Requires only one of both parameter**

Raise
-----
    ValueError
    If variable was not the expected type
    If no arguments are provided
-----

Query : method
--------------
Method used to perform a query

Parameters
----------
    query : str
    Contains the searched value

    order_settings : list[str | bool]
    Contains what to order with and direction

    filter_settings : dict[str, dict[str, List[str | int] | bool]]
    Contains what to filter with

    tags : list[str], optional
    Tags assigned when upload, by default None

Returns
-------
    Search : Search
    Contains all info about the query

Raise
-----
    ValueError
    WrongOrderStructure
    WrongFilterStructure
    WrongTagsStructure
    If variable was not the expected type
-----

Update likes : method
----------------------------
update_likes updates the like cound of a video from the `videos` list<br>
given specific parameters.

Parameters
----------
    number : int
    Number to add to the like count, can be positive or negative.

    VIDEO_ID : int, optional
    Index that leads to the video on the `videos` list, by default None

    VIDEO_FILENAME : str, optional
    Filename of the video, by default None

    **Requires only one of both Video related parameters**

Raise
-----
    ValueError
    If variable was not the expected type
    If no video related arguments are provided
```
</details>

### **uploads_manager**

```
Uploads Manager
---------------
This file contains the class UploadManager, in which we can find all methods
related with file uploads to the server.
```

<details>

```
UploadManager : class
---------------------
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
----------

Upload : method
---------------
Method used to upload files to the DataBase

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
    videos : Videos
    Contains all info about the DataBase
```

</details>



### **videos**

```
Videos
------
This file contains the class Video and Videos, which are in charge of managing
the Videos DataBase.
```

- #### **Class Video**

<details>

```
Video : class
-------------
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
----------------
Video object to dict

This property takes all values assigned to the object and<br>
transforms them into a dict

Returns
-------
    video_json : dict
    Contains all info about the Video object
```

</details>

- #### **Class Videos**

<details>

```
Videos : class
--------------
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

Load Videos : method
---------------------
Method used to load videos from the DataBase

Load_videos access the DataBase JSON file and loads all the data in
it to Video objects and dumps them into a list.

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
-------

Save Videos : method
--------------------
Method used to save videos to the DataBase

Save_videos transforms the videos list to a dictionary to then save
it to the DataBase JSON file.

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
-------

Add Videos : method
-------------------
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

Delete Video : method
---------------------
Method used to delete videos from the DataBase

Delete_video deletes a video from the videos list given specific parameters.

Parameters
----------
    VIDEO_ID : int, optional
    Index that leads to the video on the videos list, by default None

    VIDEO_FILENAME : str, optional
    Filename of the video, by default None

-> Requires only one of both parameter

Raise
-----
    IndexError
    If VIDEO_ID is not in range of amount of videos

    Exception (on self.__get_by_name)
    If VIDEO_FILENAME is not in database
-----

Like count : method
-------------------
Like_count updates the like cound of a video from the `videos` list<br>
given specific parameters.

Parameters
----------
    number : int
    Number to add to the like count, can be positive or negative.

    VIDEO_ID : int, optional
    Index that leads to the video on the `videos` list, by default None

    VIDEO_FILENAME : str, optional
    Filename of the video, by default None

    **Requires only one of both Video related parameters**

Raise
-----
    IndexError
    If VIDEO_ID is not in range of amount of videos

    Exception (on self.__get_by_name)
    If VIDEO_FILENAME is not in database
-----
```

</details>

### **SearchEngine**
```
SEARCH ENGINE
-------------
Use the custom search engine designed by Dtar380 for the VideoService library
Multilingual search engine based on percentage of coincidence of a query, with
the ability to filter and order results as user desires. Giving the ability to
the user to change query parameters as fast as possible thanks to the Search
class objects implementation.
```

#### **search_engine.py**

<details>

```
search_engine.py
----------------
Containing all functions of the search engine, this is where your search takes
place.
```

</details>

- #### **Class QueryWords**

<details>

```
QueryWords : class
------------------
The QueryWords class contains the weights for each type of word.
A QueryWords object contains the words of the query divided in
each category as well as the max weight it can have.

Parameters
----------
    query : str
    Contains the searched value

    language_dict : dict
    Contains a dictionary of the language of the query
----------
```

</details>

- #### **Functions**

<details>

```
Search : method
---------------
Function used to perform a search

Parameters
----------
    videos : list[Video]
    Contains all info about the DataBase

    query : str
    Contains the searched value

    languages_path : str
    Path to the languages DataBase

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
-------

Order : method
--------------
Function used to order the videos

Parameters
----------
    videos : list[Video]
    Contains all info about the DataBase

    order_settings : list[str | bool]
    Contains what to order with and direction

    title : str, optional
    Query, by default None

    tags : list[str], optional
    Tags assigned when upload, by default None

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
-------

Filter : method
---------------
Function used to filter the videos

Parameters
----------
    videos : list[Video]
    Contains all info about the DataBase

    filter_settings : dict[str, dict[str, List[str | int] | bool]]
    Contains what to filter with

Returns
-------
    videos : list[Video]
    Contains all info about the DataBase
-------
```

</details>

#### **Class Search**

<details>

```
Search : class
--------------
A Search object is created when ever a search is performed 
by a user, and it contains all info about the query.

Parameters
----------
    query : str
    Contains the searched value

    videos : list[Video]
    Contains all info about the DataBase

    languages_path : str
    Path to the languages DataBase

    order_settings : list[str | bool]
    Contains what to order with and direction
    Default, by Title coincidence descendant

    filter_settings : dict[str, dict[str, List[str | int] | bool]]
    Contains what to filter with
    Default, deactivated every filter

    tags : list[str], optional
    Tags assigned when upload, by default None
----------

Query Server : method
---------------------
Use when want to perform a query to the server.
Sets the class variable `result` to the result of
the query.
----------

Tags Change : method
--------------------
Use when user changed the tags of the query.
Automatically changes the result of the query.

Parameters
----------
    tags : list[str]
    Tags searched for the video

Raise
-----
    WrongTagsStructure
    If variable was not the expected type
-----

Order Settings Change : method
------------------------------
Use when user changed order settings. Automatically
changes the result of the query.

Parameters
----------
    order_settings : list[str | bool]
    List containing the parameter to use and way to order
    If Second Value True descendant order if False ascendant

Raise
-----
    WrongOrderStructure
    If variable was not the expected type
-----

Filter Settings Change : method
-------------------------------
Use when user changed filter settings. Automatically 
changes the result of the query.

Parameters
----------
    filter_settings : dict[str, dict[str, List[str | int] | bool]]
    Dict containing the parameters to use

Raise
-----
    WrongFilterStructure
    If variable was not the expected type
-----
```

</details>

#### **Query Settings**

<details>

```python
order_setting structure:
[
    str,
    True | False
]

order types:
"_order_by_title_coincidence"
"_order_by_date"
"_order_by_length"
"_order_by_tags_coincidence"
"_order_by_popularity"

-------------------------
filter_setting structure:
{
"_filter_by_date": {
    "filter": List[str],
    "active": True | False
    },
"_filter_by_length": {
    "filter": List[int],
    "active": True | False
    },
"_filter_by_tags": {
    "filter": List[str],
    "active": True | False
    }
}
```

</details>

## :open_file_folder: Known Issues
As there hasn't been a deploy yet, Im not trying to find bugs, Im just coding and testing

## :scroll: License
VideoService is distributed under the license MIT.<br>
See the [LICENSE](LICENSE) file for more information.

## :money_with_wings: Sponsorship
You can support me and the project with a donation to my Ko-Fi<br>

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/H2H4TBMEZ)
