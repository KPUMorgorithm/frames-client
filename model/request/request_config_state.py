from enum import Enum

class State(Enum):
    ACCEPT=1
    REJECT=2
    INPUTERROR=3
    SERVERERROR=4
    EXCEPTION=5