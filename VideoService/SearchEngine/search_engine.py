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
from typing import Callable
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

    def __init__(self, query: str, language_dict: dict) -> None:

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
def search(videos: list[Video], query: str, languages_path: str) -> list[Video]:

    """
    ## Search

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
    """

    language = LanguageDetectorBuilder.from_all_languages().build().detect_language_of(query)
    language_file = f"{language.iso_code_639_1.name.lower()}.json"
    language_dict = path.join(languages_path, language_file)

    with open(language_dict, "r+", encoding="utf-8") as f:
        data = json.load(f.read())

    query_words = QueryWords(query, data)
    videos = _filter_by_query(videos, query_words)

    return videos

def _filter_by_query(videos: list[Video], query_words: QueryWords) -> list[Video]:
    threshold = query_words.max_score * 0.25

    word_weights = [{word: QueryWords.weights[i] for word in words}
        for i, words in enumerate(query_words.words)]

    return [video for video in videos if sum(weight
        for i, words in enumerate(word_weights)
        for word, weight in words.items()
        if word in video.TITLE
        ) >= threshold]

def order(order_settings: list, videos: list[Video], title: str = None, tags: list[str] = None) -> list[Video]:
    
    """
    ## Order

    Function used to order the videos

    Parameters
    ----------
    order_settings : list
        Contains what to order with and direction

    videos : list[Video]
        Contains all info about the DataBase

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

def _order_by_title_coincidence(videos: list[Video], title: str, order: bool = True) -> list[Video]: 
    return sorted(videos, key=lambda video: sum(1 for word in title.split(" ") if word in video.TITLE), reverse=order)

def _order_by_date(videos: list[Video], order: bool = True) -> list[Video]:
    return videos.sort(key=lambda x: x.UPLOAD_DATE, reverse=order)

def _order_by_length(videos: list[Video], order: bool = True) -> list[Video]:
    return videos.sort(key=lambda x: x.LENGTH, reverse=order)

def _order_by_tags_coincidence(videos: list[Video], tags: list[str], order: bool = True) -> list[Video]:
    return sorted(videos, key=lambda video: sum(1 for tag in tags if tag in video.TAGS), reverse=order)

def _order_by_popularity(videos: list[Video], order: bool = True) -> list[Video]:
    return videos.sort(key=lambda x: x.LIKES, reverse=order)

def filter(filter_settings: dict, videos: list[Video]) -> list[Video]:
    
    """
    ## Filter

    Function used to filter the videos

    Parameters
    ----------
    filter_settings : dict
        Contains what to filter with

    videos : list[Video]
        Contains all info about the DataBase

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

def _filter_by_date(videos: list[Video], filter: list[str]) -> list[Video]:
    if len(filter) != 2:
        raise "ERROR [SEARCH_ENGINE]: Filter list does not contain the requested amount of items"
    
    if filter[1] == "0":
        return [video for video in videos if filter[0] < video.UPLOAD_DATE]
    elif filter[0] == "0":
        return [video for video in videos if video.UPLOAD_DATE < filter[1]]
    else:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE < filter[1]]


def _filter_by_length(videos: list[Video], filter: list[int]) -> None:
    if len(filter) != 2:
        raise "ERROR [SEARCH_ENGINE]: Filter list does not contain the requested amount of items"
    
    if filter[1] == 0:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE]
    else:
        return [video for video in videos if filter[0] < video.UPLOAD_DATE < filter[1]]

def _filter_by_tags(videos: list[Video], filter: list[str]) -> None:
        return [video for video in videos if filter in video.TAGS]