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

    def get_attacker(self) -> PlayerID:
        return self.current_player
    
    def get_defender(self) -> PlayerID:
        for player in self.players:
            if player != self.current_player:
                return player

    def get_ships_to_place(self, player: PlayerID) -> List[ShipType]:
        return self.ships_to_place.get(player)
    
    def get_board_size(self) -> int:
        return self.board_size
    
    def get_board(self, player: PlayerID) -> Board:
        return self.board_map[player]

