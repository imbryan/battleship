from enum import Enum
import random


class PlayerID(Enum):
    HUMAN = 'human'
    AI = 'ai'


class ShipPlacementStatus(Enum):
    SUCCESS = 0
    INVALID = 1


class Orientation(Enum):
    HORIZONTAL = 'H'
    VERTICAL = 'V'

    @classmethod
    def random(cls):
        return random.choice(list(cls))


class ShipType(Enum):
    CARRIER = 5
    BATTLESHIP = 4
    CRUISER = 3
    SUBMARINE = 3
    DESTROYER = 2


class ShotStatus(Enum):
    MISS = 'Miss'
    HIT = 'Hit'
    UNSHOT = 'Unshot'
    ALREADY_SHOT = 'Already_Shot'
    INVALID = 'Invalid'
