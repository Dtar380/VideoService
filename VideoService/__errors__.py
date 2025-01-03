
#################################################*
##### ***  IMPORTS  *** #########################*
#################################################*

# *** Python modules *** #
import os

#################################################*
##### ***  CODE  ***    #########################*
#################################################*

### *** ERROR CLASSES *** ###
## *** NOT FOUND ERROR *** ##
class NotFoundError(Exception):

    """
    NotFoundError
    =============
    Exception raised when a resource is not found.

    Parameters
    ----------
    message : str
        Error message.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

## *** ALREADY EXISTS ERROR *** ##
class AlreadyExistsError(Exception):

    """
    AlreadyExistsError
    ==================
    Exception raised when a resource already exists.

    Parameters
    ----------
    message : str
        Error message.
    """

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

### *** FUNCTIONS *** ###
## *** ERROR PARSER *** ##
def error_parser(error: str) -> str:

    """
    Error Parser
    ============
    Function to parse an error message.

    Parameters
    ----------
    error : str
        Error message.

    Returns
    -------
    error_str : str
        Parsed error message.
    """

    # Convert the error to a string
    error = repr(error)

    # Check if error uses ' or "
    if "('" in error:
        error_str = error.replace("('", ": ").replace("')", "") # Replace ' with :
    elif "(\"" in error:
        error_str = error.replace("(\"", ": ").replace("\")", "") # Replace " with :
    else:
        error_str = error # Return the error

    return error_str

## *** ARGS HANDLING *** ##
def args_handling(init: bool, **kwargs):

    """
    Args Handling
    =============
    Function to handle the arguments.

    Parameters
    ----------
    init : bool
        If the function is called from the __init__ method.

    **kwargs : dict
        Keyword arguments.

    Raises
    ------
    TypeError
        If all values are not of type `str`.

        If `TAGS` is not of type `list`.

        If all values in `TAGS` are not of type `str`.

    NotFoundError
        If the folder does not exist.
    """

    # Values without TAGS
    values = [value[1] for value in kwargs.items() if value[0] != "TAGS"]

    # Check if all values are strings
    if not all(isinstance(value, str) for value in values):
        raise TypeError("ERROR [VideoService]: All values must be of type 'str'")

    if init:
        if not all(os.path.exists(value) for value in values):
            raise NotFoundError("ERROR [VideoService]: The folder does not exist")

    # Check if TAGS is in kwargs
    if kwargs.get("TAGS"):

        # Check if TAGS is a list
        if not isinstance(kwargs.get("TAGS"), list):
            raise TypeError("ERROR [VideoService]: 'TAGS' must be of type 'list'")

        # Check if all values in TAGS are strings
        if not all(isinstance(tag, str) for tag in kwargs.get("TAGS")):
            raise TypeError("ERROR [VideoService]: All values in 'TAGS' must be of type 'str'")
