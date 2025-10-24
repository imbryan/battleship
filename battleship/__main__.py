from . import view
from .ai_strategy import RandomStrategy
from .enums import PlayerID, ShipPlacementStatus, ShotStatus
from .engine import BattleshipGame
from .models import Board

def setup_game():
    board_size = view.read_board_size()
    ai_strategy = RandomStrategy(board_size=board_size)
    player1_board = Board(board_size)
    player2_board = Board(board_size)
    engine = BattleshipGame(
        board_size,
        (PlayerID.HUMAN, PlayerID.AI),
        {
            PlayerID.HUMAN: player1_board,
            PlayerID.AI: player2_board,
        },
        ai_strategy,
    )
    # SHIP PLACEMENT
    engine.simulate_placement()
    while not engine.is_placement_complete():
        ship_type, coord, ornt = view.read_ship_placement(board_size=board_size, ship_types=engine.get_ships_to_place(PlayerID.HUMAN))
        status = engine.place_ship(PlayerID.HUMAN, ship_type, coord, ornt)
        if status == ShipPlacementStatus.INVALID:
            view.show_message("Invalid ship placement! Try again.")
    return engine

def main():
    view.show_message("Welcome to Battleship!")
    engine = setup_game()
    while not engine.get_winner():
        current_player = engine.get_attacker()
        if current_player == PlayerID.AI:
            shot_status, sunk = engine.simulate_turn()
        elif current_player == PlayerID.HUMAN:
            target = view.read_coord(engine.get_board_size())
            shot_status, sunk = engine.fire_shot(current_player, target)
            if shot_status == ShotStatus.ALREADY_SHOT:
                view.show_message(f"You already shot at {target}! Try again.")
                continue
            elif shot_status == ShotStatus.INVALID:
                view.show_message("Invalid shot target! Try again.")
                continue
        view.show_message(f"{current_player} fired a shot. It's a {shot_status.value}!")
        if sunk:
            view.show_message(f"{engine.get_defender()}'s {sunk} sunk!")

if __name__ == "__main__":
    main()
