from enum import IntEnum

class ExitCodes(IntEnum):

    SUCCESS = 0
    VALIDATION_ERROR = 1
    ARGUMENT_ERROR = 2
    DIFF_ERROR = 3
    OTHER_ERROR = 4