class NotFoundError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AlreadyExistsError(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def error_parser(error: str) -> str:
    error = repr(error)
    if "('" in error:
        error_str = error.replace("('", ": ").replace("')", "")
    else:
        error_str = error.replace("(\"", ": ").replace("\")", "")
    return error_str
