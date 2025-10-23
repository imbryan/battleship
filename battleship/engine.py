from typing import Dict, List, Optional, Tuple

from .ai_strategy import AIStrategy
from .enums import PlayerID, ShipPlacementStatus
from .models import Coordinate, ShotStatus, ShipType, Board, Orientation



class BattleshipGame:
    board_size: int
    board_map: Dict[PlayerID, Board]
    ai_strategy: Optional[AIStrategy]
    players: Tuple[PlayerID]
    current_player: PlayerID
    ships_to_place: Dict[PlayerID, List[ShipType]]

    def __init__(
            self,
            board_size: int,
            players: Tuple[PlayerID],
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
    ) -> ShipPlacementStatus:
        pass

    def simulate_placement(self):
        pass

    def is_placement_complete(self) -> bool:
        pass

    def fire_shot(
            self, 
            attacker: PlayerID,
            target_coord: Coordinate
    ) -> Tuple[ShotStatus, Optional[str]]:
        pass

    def simulate_turn(self) -> Tuple[ShotStatus, Optional[str]]:
        pass

    def next_turn(self):
        pass

    def get_winner(self) -> Optional[PlayerID]:
        pass
