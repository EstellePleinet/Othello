from typing import Optional
from .player import Player
from .pawn import Pawn, Color
from .position import Position, Direction
from .board import Board, Move

"""A class representing a game of Othello (Reversi)."""
class Game:
    
    def __init__(self, player_one: Player, player_two: Player, size=8):
        if not isinstance(player_one, Player) or not isinstance(player_two, Player):
            raise ValueError("Both players must be instances of Player.")
        
        self._board = Board(size)
        self._players = [player_one, player_two]
        self._current_player_index = 0
        self._is_over = False
        self._winner = None
    
    @property
    def board(self) -> Board:
        return self._board
    
    @property
    def players(self) -> list[Player]:
        return self._players
    
    @property
    def current_player(self) -> Player:
        return self.players[self._current_player_index]
    
    @property
    def is_over(self) -> bool:
        return self._is_over
    
    @property
    def winner(self) -> Optional[Player]:
        return self._winner
    
    def switch_turn(self):
        self._current_player_index = 1 - self._current_player_index
        
    def update_winner(self):
        """Updates the winner of the game if it is finished."""
        if self.is_over:
            black_pawns = self.board.cases_with_pawn_color(Color.BLACK)
            white_pawns = self.board.cases_with_pawn_color(Color.WHITE)
            if len(black_pawns) > len(white_pawns):
                self._winner = self.players[0]
            elif len(white_pawns) > len(black_pawns):
                self._winner = self.players[1]
            else:
                self._winner = None
    
    def update_is_over(self):
        possible_moves_black = self.board.valid_moves_iterator(Color.BLACK)
        possible_moves_white = self.board.valid_moves_iterator(Color.WHITE)
        self._is_over = self.board.is_full() or (not (possible_moves_black or possible_moves_white))
        
    def game_is_over(self) -> bool:
        self.update_is_over()
        return self._is_over
    
    def game_evaluate(self, color: Color) -> int:
        """Evaluates the game state for the given color."""
        
        black_pawns = len(self.board.cases_with_pawn_color(Color.BLACK))
        white_pawns = len(self.board.cases_with_pawn_color(Color.WHITE))
        
        if color == Color.BLACK:
            return black_pawns - white_pawns
        elif color == Color.WHITE:
            return white_pawns - black_pawns


    def validate_move(self, pos_str: str, player: Player) -> tuple[Position, Color, list[Move]]:
        """Validates a move and returns data needed to play it, or raises ValueError."""
        if self.is_over:
            raise ValueError("The game is over. No more moves can be played.")
        
        if player != self.current_player:
            raise ValueError("It's not your turn.")
        
        if not Position.is_valid_label_format(pos_str):
            raise ValueError("Invalid position format. Use a letter followed by a number (e.g., A1, B2).")
        
        position = Position(label=pos_str.strip().upper())

        if not self.board.is_valid_position(position):
            raise ValueError("The position is out of bounds of the board.")
        
        if self.board.case_at(position).pawn is not None:
            raise ValueError("The position is already occupied by a pawn.")

        color = player.color

        # Vérifie qu’il existe des coups possibles
        if not any(self.board.valid_moves_iterator(color)):
            raise ValueError(f"No valid moves available for {player.name}.")

        # Récupère uniquement les coups liés à cette position
        compatible_moves = [m for m in self.board.valid_moves_iterator(color) if m.starting_position == position]

        if not compatible_moves:
            raise ValueError("No valid move at this position.")

        return position, color, compatible_moves

    
    def play_turn(self, pos_str: str, player: Player) -> bool:
        """Plays a turn for the given player at the specified position."""
        position, color, compatible_moves = self.validate_move(pos_str, player)
        return self.play_move(position, color, compatible_moves)

   
    def play_move(self, pos: Position, color: Color, compatible_moves: list[Move]) -> bool:
        """Plays a move at the specified position with the given color and compatible flips."""
        self.board.case_at(pos).pawn = Pawn(color)
        self.board.flip_pawns(compatible_moves)

        self.update_is_over()
        if not self.is_over:
            self.switch_turn()
        else:
            self.update_winner()

        return True


