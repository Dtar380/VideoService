
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

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

## *** ALREADY EXISTS ERROR *** ##
class AlreadyExistsError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

### *** FUNCTIONS *** ###
## *** ERROR PARSER *** ##
def error_parser(error: str) -> str:
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
