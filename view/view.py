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
        
    @staticmethod
    def ask_bot():
        return input("Do you want to play against a bot? (yes/[no]): ").strip().lower() in ['yes', 'y', 'oui', 'o']
    
    @staticmethod
    def ask_color():
        color = input("Choose your color (black/white): ").strip().lower()
        if color not in ['black', 'b', 'noir', 'n', 'white', 'w', 'blanc', 'b', 'bl', '']:
            raise ValueError("Invalid color choice. Please choose 'black' or 'white'.")
        return color
    
    @staticmethod
    def ask_difficulty():
        difficulty = input("Choose bot difficulty (1, 2, 3 or 4): ").strip().lower()
        if difficulty not in ['1', '2', '3', '4']:
            raise ValueError("Invalid difficulty choice. Please choose '1', '2', '3', '4' ")
        return difficulty