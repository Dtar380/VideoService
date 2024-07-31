########################################
#####  DOCUMENTATION               #####
########################################

"""
search_engine.py
----------------
Containing all functions of the search engine, this is where your search takes <br>
place.
"""

########################################
#####  IMPORTING MODULES           #####
########################################

#####  EXTERNAL IMPORTS

# PYTHON BUILT-IN
from typing import List
from os import path
import json

# LIBRARIES
from lingua import LanguageDetectorBuilder

#####  INTERNAL IMPORTS
from ..videos import Video

########################################
#####  CODE                        #####
########################################

#####  CLASS
class QueryWords:

    """
    QueryWords
    ----------
    The QueryWords class contains the weights for each type of word. <br>
    A QueryWords object contains the words of the query divided in <br>
    each category as well as the max weight it can have.
    """

    weights = [4, 4, 4, 4, 3, 3, 2, 2, 1, 1]

    def __init__(self,
        query: str,
        language_dict: dict
        ) -> None:

        """
        ## Constructor function of QueryWords class

        Parameters
        ----------
        query : str
            Contains the searched value

        language_dict : dict
            Contains a dictionary of the language of the query
        """

        query_list = query.lower().split(" ")

        dict_sets = {key: set(words) for key, words in language_dict.items()}

        names = []
        verbs = []
        nouns = []
        adverbs = []
        adjectives = []
        pronouns = []
        determiners = []
        prepositions = []
        interjections = []
        conjunctions = []

        for word in query_list:
            for category in dict_sets:
                if word in dict_sets[category]:
                    locals()[category].append(word)
                    break
            else:
                names.append(word)

        self.words = [
            names,
            verbs,
            nouns,
            adverbs,
            adjectives,
            pronouns,
            determiners,
            prepositions,
            interjections,
            conjunctions
        ]

        word_weights = [
            {word: self.weights[i] for word in words}
            for i, words in enumerate(self.words)
        ]

        self.max_score = sum(
            weight for i, words in enumerate(word_weights)
            for word, weight in words.items()
        )

#####  FUNCTIONS
def search(videos: List[Video], query: str, LANGUAGES: str) -> List[Video]:

    """
    ## Search

    Function used to perform a search

    Parameters
    ----------
    videos : list[Video]
        Contains all info about the DataBase

    query : str
        Contains the searched value

    LANGUAGES : str
        Path to the languages DataBase

    Returns
    -------
    videos : list[Video]
        Contains all info about the DataBase
    """

    language = LanguageDetectorBuilder.from_all_languages().build().detect_language_of(query)
    language_file = f"{language.iso_code_639_1.name.lower()}.json"
    language_dict = path.join(LANGUAGES, language_file)

    with open(language_dict, "r+", encoding="utf-8") as f:
        data = json.load(f.read())

    query_words = QueryWords(query, data)
    videos = _filter_by_query(videos, query_words)

    return videos

def _filter_by_query(videos: List[Video], query_words: QueryWords) -> List[Video]:
    threshold = query_words.max_score * 0.25

    word_weights = [{word: QueryWords.weights[i] for word in words}
        for i, words in enumerate(query_words.words)]

    return [video for video in videos if sum(weight
        for i, words in enumerate(word_weights)
        for word, weight in words.items()
        if word in video.TITLE
        ) >= threshold]

def order(videos: List[Video], 
    order_settings: list,
    title: str = None,
    tags: List[str] = None
    ) -> List[Video]:
    
    """
    ## Order

    Function used to order the videos

    Parameters
    ----------
    videos : list[Video]
        Contains all info about the DataBase

    order_settings : list
        Contains what to order with and direction

    title : str, optional
        Query, by default None

    tags : list[str], optional
        Tags assigned when upload, by default None

    Returns
    -------
    videos : list[Video]
        Contains all info about the DataBase
    """

    if order_settings[0] == "TITLE":
        return _order_by_title_coincidence(videos, title, order_settings[1])
    elif order_settings[0] == "UPLOAD_DATE":
        return _order_by_date(videos, order_settings[1])
    elif order_settings[0] == "LENGTH":
        return _order_by_length(videos, order_settings[1])
    elif order_settings[0] == "TAGS":
        return _order_by_tags_coincidence(videos, tags, order_settings[1])
    elif order_settings[0] == "LIKES":
        return _order_by_popularity(videos, order_settings[1])

def _order_by_title_coincidence(videos: List[Video], title: str, order: bool = True) -> List[Video]: 
    return sorted(videos, key=lambda video: sum(1 for word in title.split(" ") if word in video.TITLE), reverse=order)

def _order_by_date(videos: List[Video], order: bool = True) -> List[Video]:
    return videos.sort(key=lambda x: x.UPLOAD_DATE, reverse=order)

def _order_by_length(videos: List[Video], order: bool = True) -> List[Video]:
    return videos.sort(key=lambda x: x.LENGTH, reverse=order)

def _order_by_tags_coincidence(videos: List[Video], tags: List[str], order: bool = True) -> List[Video]:
    return sorted(videos, key=lambda video: sum(1 for tag in tags if tag in video.TAGS), reverse=order)

def _order_by_popularity(videos: List[Video], order: bool = True) -> List[Video]:
    return videos.sort(key=lambda x: x.LIKES, reverse=order)

def filter(videos: List[Video], filter_settings: dict) -> List[Video]:
    
    """
    ## Filter

    Function used to filter the videos

    Parameters
    ----------
    videos : list[Video]
        Contains all info about the DataBase

    filter_settings : dict
        Contains what to filter with

    Returns
    -------
    videos : list[Video]
        Contains all info about the DataBase

    """

    filters = {
        '_filter_by_date': _filter_by_date,
        '_filter_by_length': _filter_by_length,
        '_filter_by_tags': _filter_by_tags
    }

    for filter_name, settings in filter_settings.items():
        if settings["active"]:
            videos = filters[filter_name](videos, settings["filter"])
    
    return videos

def _filter_by_date(videos: List[Video], filter: List[str]) -> List[Video]:
    if filter[1] == "0":
        return [video for video in videos if filter[0] < video.UPLOAD_DATE]
    elif filter[0] == "0":
        return [video for video in videos if video.UPLOAD_DATE < filter[1]]
    else:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE < filter[1]]


def _filter_by_length(videos: List[Video], filter: List[int]) -> None:
    if filter[1] == 0:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE]
    else:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE < filter[1]]

def _filter_by_tags(videos: List[Video], filter: List[str]) -> None:
        return [video for video in videos if filter in video.TAGS]