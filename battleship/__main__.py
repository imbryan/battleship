from . import view
from .ai_strategy import RandomStrategy
from .enums import PlayerID, ShipPlacementStatus, ShotStatus
from .engine import BattleshipGame
from .models import Board

def setup_game():
    while True:
        try:
            board_size = view.read_board_size()
            break
        except view.InvalidInputError as e:
            view.show_message(e)
            continue
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
    engine.initialize_placement()
    engine.simulate_placement()
    while not engine.is_placement_complete():
        view.draw_board(engine.get_board(PlayerID.HUMAN))
        try:
            ship_type = view.read_ship_type(ship_types=engine.get_ships_to_place(PlayerID.HUMAN))
            coord = view.read_coord(board_size=board_size)
            ornt = view.read_orientation()
            status = engine.place_ship(PlayerID.HUMAN, ship_type, coord, ornt)
        
            if status == ShipPlacementStatus.INVALID:
                raise view.InvalidInputError("Invalid ship placement! Try again.")
        except view.InvalidInputError as e:
            view.show_message(e)
            continue
        # Give option to redo placement
        if engine.is_placement_complete():
            view.draw_board(engine.get_board(PlayerID.HUMAN))
            if not view.confirm("Confirm placements"):
                engine.initialize_placement()
                engine.simulate_placement()
                continue
    return engine

def main():
    view.show_message("Welcome to Battleship!")
    engine = setup_game()
    while not engine.get_winner():
        current_player = engine.get_attacker()
        # AI TURN
        if current_player == PlayerID.AI:
            shot_status, sunk_ship = engine.simulate_turn()
        # HUMAN TURN
        elif current_player == PlayerID.HUMAN:
            try:
                target = view.read_coord(engine.get_board_size())
                shot_status, sunk_ship = engine.fire_shot(current_player, target)
                if shot_status == ShotStatus.ALREADY_SHOT:
                    raise view.InvalidInputError(f"You already shot at {target}! Try again.")
            except view.InvalidInputError as e:
                view.show_message(e)
                continue
        # BROADCAST SHOT INFORMATION
        view.show_message(f"{current_player} fired a shot. It's a {shot_status.value}!")
        if sunk_ship:
            view.show_message(f"{engine.get_defender()}'s {sunk_ship} sunk!")

if __name__ == "__main__":
    main()
