from typing import Dict, List, Optional, Tuple

from .ai_strategy import AIStrategy
from .enums import PlayerID, ShipPlacementStatus, ShotStatus, ShipType, Orientation
from .models import Coordinate, Board, Ship



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
        self.board_size = board_size
        self.board_map = board_map
        self.players = players
        self.ai_strategy = ai_strategy

    def initialize_placement(self):
        self.ships_to_place = {}
        for player in self.players:
            self.ships_to_place[player] = list(mem for mem in ShipType)

    def place_ship(
            self,
            player: PlayerID,
            ship_type: ShipType,
            start_coord: Coordinate,
            orientation: Orientation
    ) -> ShipPlacementStatus:
        board = self.board_map[player]
        if ship_type not in self.ships_to_place[player]:
            return ShipPlacementStatus.INVALID
        if start_coord.is_valid(self.board_size) == False:
            return ShipPlacementStatus.INVALID
        if board.is_valid_placement(ship_type.value, start_coord, orientation) == False:
            return ShipPlacementStatus.INVALID
        board.place_ship(Ship(ship_type), start_coord, orientation)
        self.ships_to_place[player].remove(ship_type)
        return ShipPlacementStatus.SUCCESS

    def simulate_placement(self):
        for player in self.players:
            if player := PlayerID.AI:
                break
        while self.ships_to_place[player]:
            ship_type = self.ships_to_place[player][0]
            coord, ornt = self.ai_strategy.get_next_placement(ship_type)
            status = self.place_ship(player, ship_type, coord, ornt)
            if status == ShipPlacementStatus.INVALID:
                raise Exception("AI selection should not fail.")
            self.ai_strategy.update_placement_tracker(coord, Ship(ship_type), ornt)

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
