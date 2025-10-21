from typing import Dict, List, Optional, Tuple

from .ai_strategy import AIStrategy
from .models import Coordinate, ShotStatus, ShipType, Board, PlayerID, Orientation

class InvalidPlacementError(Exception):
    pass


class BattleshipGame:
    board_size: int
    board_map: Dict[PlayerID, Board]
    ai_strategy: Optional[AIStrategy]
    current_player: PlayerID
    ships_to_place: Dict[PlayerID, List[ShipType]]

    def __init__(
            self,
            board_size: int,
            board_map: Dict[PlayerID, Board],
            ai_strategy: Optional[AIStrategy]):
        pass

    def initialize_placement(self):
        pass

    def place_ship(
            self,
            player: PlayerID,
            ship_type: ShipType,
            start_coord: Coordinate,
            orientation: Orientation
    ):
        pass

    def is_placement_complete(self) -> bool:
        pass

    def fire_shot(
            self, 
            attacker: PlayerID,
            target_coord: Coordinate
    ) -> Tuple[ShotStatus, Optional[str]]:
        pass

    def get_ai_shot_result(self) -> Tuple[Coordinate, ShotStatus, Optional[str]]:
        pass

    def get_winner(self) -> Optional[PlayerID]:
        pass
