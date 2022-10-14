from enum import Enum


class ExperienceLevel(Enum):
    BEGINNER = "Beginner"
    MEDIUM = "Intermédiaire"
    EXPERT = "Expert"


class Action(Enum):
    PHYSICAL = 1
    SPELL = 2
    CHAT = 3


class Status(Enum):
    CONTINUE = "Continue"
    STOP = "Stop"


class CharacterType(Enum):
    MENTOR = "Mentor"
    BACHELOR = "Bachelor"


class GameFeature(Enum):
    PVP = 1
    PVE = 2
    QUIT = 3
