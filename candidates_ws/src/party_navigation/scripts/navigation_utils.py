from enum import Enum

class Behaviors(Enum):
    Patrol = 1
    Stop = 2

class StatusMessage(Enum):
    Failed = 0
    Busy = 1
    Success = 2
