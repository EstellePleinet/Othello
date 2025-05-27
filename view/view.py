from model import Board, Player

class View:

    @staticmethod
    def display_board(board: Board):
        print(board)

    @staticmethod
    def ask_move(player: Player) -> str:
        return input(f"{player}, enter your move (e.g., D3): ").strip()

    @staticmethod
    def ask_player_name(number: int) -> str:
        return input(f"Player {number}, enter your name: ").strip()

    @staticmethod
    def display_error(message: str):
        print(f"Error: {message}")

    @staticmethod
    def display_message(message: str):
        print(message)
